#coding=utf-8
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.http import HttpResponse

from plays.models import Team, Person


def login(request):
    state = "Please log in below..."
    username = password = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect('/issueapp/1628/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response(
        'login.html',
        {
        'state':state,
        'username': username
        },
        context_instance=RequestContext(request)
    )


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


def player_details(request, player_id):
    player = Person.objects.get(id=int(player_id))
    return render_to_response('player.html',
                              {'player': player})
