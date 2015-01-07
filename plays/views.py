#coding=utf-8
# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

from plays.models import Team, Person, Match, Goal, Card


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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cabinet(request):
    print "cabinet hit"
    person = request.user.person
    now = datetime.now()
    matches = Match.objects.filter(Q(home_team=person.team) | Q(guest_team=person.team), date__gte=now.date()).\
        order_by('date')[0:3]
    for match in matches:
        match.intended = True if match in person.matches_intended.all() else False

    person.goals = Goal.objects.filter(player_scored=person).count()
    person.assists = Goal.objects.filter(player_assisted=person).count()

    return render_to_response('cabinet.html',
                              {'person': person,
                               'matches': matches})


@login_required()
def cabinet_update_model(request):
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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cabinet_all_matches(request):
    match_today = None
    person = request.user.person
    now = datetime.now()
    matches_played = person.matches_played.all()
    matches_absent = Match.objects.filter(date__lt=now.date()).\
        exclude(id__in=matches_played.values_list('id', flat=True))

    match_list_past = []

    try:
        match_today = Match.objects.get(date=now.date())
        match_today.type = "today"
    except ObjectDoesNotExist:
        pass
    matches_future = Match.objects.filter(date__gt=now.date())

    # if changing type here, change type in corresponding template
    for e in matches_played:
        e.type = "played"
        match_list_past.append(e)

    for e in matches_absent:
        e.type = "absent"
        match_list_past.append(e)

    for e in matches_future:
        e.type = "future"
        e.intended = "checked" if e in person.matches_intended.all() else ""

    resp_dict = {'matches_past': match_list_past,
                               'matches_future': matches_future,
                               'match_today': match_today}

    match_list_past.sort(key=lambda x: x.date)
    return render_to_response('cabinet_matches.html',
                              resp_dict)


def player_details(request, player_id):
    player = Person.objects.get(id=int(player_id))
    return render_to_response('player.html',
                              {'player': player})


def match_details_add_item(request, match_id, item):
    print item
    pass



@login_required()
def match_details(request, id):
    match = Match.objects.get(id=id)
    cards = Card.objects.filter(match=match).order_by("minute")
    goals = Goal.objects.filter(match=match).order_by("minute")
    players_home_played = Person.objects.filter(team=match.home_team).filter(matches_played__in=[match])
    players_guest_played = Person.objects.filter(team=match.guest_team).filter(matches_played__in=[match])

    resp_dict = {'match': match,
                 'cards': cards,
                 'goals': goals,
                 'players_home': players_home_played,
                 'players_guest': players_guest_played}

    is_user_home = request.user.person in Person.objects.filter(team=match.home_team)
    resp_dict['is_user_home'] = is_user_home
    resp_dict['user'] = request.user

    user_team = match.home_team if is_user_home else match.guest_team

    home_is_staff = False
    guest_is_staff = False


    # Admin section
    if request.user.is_staff:
        home_is_staff = is_user_home
        guest_is_staff = not is_user_home

    resp_dict['home_is_stuff'] = home_is_staff
    resp_dict['guest_is_staff'] = guest_is_staff
    resp_dict.update(csrf(request))
    return render_to_response('match_details.html',
                              resp_dict)