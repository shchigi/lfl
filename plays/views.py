#coding=utf-8
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
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
    return render_to_response('cabinet.html',
                              {'matches': matches})


def player_details(request, player_id):
    player = Person.objects.get(id=int(player_id))
    return render_to_response('player.html',
                              {'player': player})
