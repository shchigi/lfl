# -*- coding: utf-8 -*-
__author__ = 'rakot'


import datetime
from models import Person, Team, Match, Card, Goal


def add_test_data():
    mipt_team = Team(name=u"Физтех", start_date=datetime.date.today())
    mipt_team.save()

    anytime_team = Team(name=u"Энитайм", start_date=datetime.date.today())
    anytime_team.save()

    den = Person(first_name=u"Денис",
                 last_name=u"Щигельский",
                 position=Person.BACK,
                 is_active=True,
                 is_captain=False,
                 start_date=datetime.date.today(),
                 cell_phone=u"+79151164158",
                 email=u"denis.shchigelsky@gmail.com",
                 team=mipt_team)
    den.save()

    stan = Person(first_name=u"Илья",
                 last_name=u"Станиславский",
                 position=Person.HALFBACK,
                 is_active=True,
                 is_captain=False,
                 start_date=datetime.date.today(),
                 cell_phone=u"+79670614948",
                 team=mipt_team)
    stan.save()

    burov = Person(first_name=u"Александр",
                 last_name=u"Буров",
                 position=Person.FORWARD,
                 is_active=True,
                 is_captain=True,
                 start_date=datetime.date.today(),
                 cell_phone=u"89197711249",
                 team=mipt_team)
    burov.save()

    ahyan = Person(first_name=u"Ара",
                   last_name=u"Ахян",
                   position=Person.FORWARD,
                   is_active=True,
                   is_captain=True,
                   start_date=datetime.date.today(),
                   cell_phone=u"89123711249",
                   team=anytime_team)
    ahyan.save()

    mipt_anytime = Match(date=datetime.date.today(),
                     time=datetime.datetime.now(),
                     home_team=mipt_team,
                     guest_team=anytime_team,
                     guest_team_score=0,
                     home_team_score=0)
    mipt_anytime.save()

    anytime_mipt = Match(date=datetime.date.today().replace(day=30),
                     time=datetime.datetime.now(),
                     home_team=anytime_team,
                     guest_team=mipt_team,
                     guest_team_score=0,
                     home_team_score=0)
    anytime_mipt.save()

    g1 = Goal(player_scored=stan,
              player_assisted=burov,
              own_goal=False,
              match=mipt_anytime,
              minute=11,
              is_penalty=False)
    g1.save()
    print mipt_anytime.home_team_score, mipt_anytime.guest_team_score


    g2 = Goal(player_scored=stan,
              player_assisted=den,
              own_goal=False,
              match=mipt_anytime,
              minute=15,
              is_penalty=False)
    g2.save()
    print mipt_anytime.home_team_score, mipt_anytime.guest_team_score

    g3 = Goal(player_scored=burov,
              own_goal=True,
              match=mipt_anytime,
              minute=58,
              is_penalty=False)
    g3.save()
    print mipt_anytime.home_team_score, mipt_anytime.guest_team_score

    g4 = Goal(player_scored=ahyan,
              own_goal=False,
              match=mipt_anytime,
              minute=59,
              is_penalty=False)
    g4.save()
    print mipt_anytime.home_team_score, mipt_anytime.guest_team_score

    card1 = Card(type='Y',
                 person=den,
                 minute=24)
    card1.save()