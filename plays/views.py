#coding=utf-8
# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from plays.models import Team, Person, Match


def index(request):
    return render_to_response('index.html')

@login_required()
def roster(request):
    person = request.user.person
    team = Team.objects.get(name=person.team)
    players = Person.objects.filter(team=team).order_by('first_name')

    team_name = team.name
    return render_to_response('roster.html',
                              {'team_name': team_name,
                               'players': players})


@login_required()
def cabinet(request):
    person = request.user.person
    matches = Match.objects.filter(Q(home_team=person.team) | Q(guest_team=person.team))
    for match in matches:
        match.intended = "checked" if match in person.matches_intended.all() else ""

    return render_to_response('cabinet.html',
                              {'matches': matches})


@login_required()
def cabinet_update_model(request):
    print request.POST.items()
    person = request.user.person
    for item in request.POST.items():
        if item[1] == "true":  # obtained from ajax in cabinet.html
            person.matches_intended.add(Match.objects.get(id=item[0]))
        else:
            try:
                match = Match.objects.get(id=item[0])
                person.matches_intended.remove(match)
            except ObjectDoesNotExist:
                pass  # just to remove matches player was not intended to play
    person.save()
    return HttpResponse("OK", status=200)


@login_required()
def cabinet_all_matches(request):
    match_today = None
    person = request.user.person
    now = datetime.now()
    matches_played = person.matches_played.all()
    matches_absent = Match.objects.filter(date__lt=now.date()).\
        exclude(id__in=matches_played.values_list('id', flat=True))
    try:
        match_today = Match.objects.get(date=now.date())
    except ObjectDoesNotExist:
        pass
    matches_future = Match.objects.filter(date__gt=now.date())

    match_list = []
    for e in matches_played:
        e.type = "played"
        match_list.append(e)

    for e in matches_absent:
        e.type = "absent"
        match_list.append(e)

    for e in matches_future:
        e.type = "future"
        match_list.append(e)

    match_today.type = "today"
    match_list.append(match_today)

    match_list.sort(key=lambda x: x.date)
    print match_list
    return render_to_response('cabinet_matches.html',
                              {'matches': match_list,
                               'match_today': match_today})


def player_details(request, player_id):
    player = Person.objects.get(id=int(player_id))
    return render_to_response('player.html',
                              {'player': player})
