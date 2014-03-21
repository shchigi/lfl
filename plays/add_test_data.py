# -*- coding: utf-8 -*-
__author__ = 'rakot'


import datetime
from models import Person, Team


def add_test_data():
    t = Team(name="Физтех", start_date=datetime.date.today())
    t.save()

    t2 = Team(name="Энитайм", start_date=datetime.date.today())
    t2.save()

    den = Person(first_name="Денис",
                 last_name="Щигельский",
                 position=Person.BACK,
                 is_active=True,
                 is_captain=False,
                 start_date=datetime.date.today(),
                 cell_phone="+79151164158",
                 email="denis.shchigelsky@gmail.com",
                 team=t)
    den.save()

    stan = Person(first_name="Илья",
                 last_name="Станиславский",
                 position=Person.HALFBACK,
                 is_active=True,
                 is_captain=False,
                 start_date=datetime.date.today(),
                 cell_phone="+79670614948",
                 team=t)
    stan.save()

    burov = Person(first_name="Александр",
                 last_name="Буров",
                 position=Person.FORWARD,
                 is_active=True,
                 is_captain=True,
                 start_date=datetime.date.today(),
                 cell_phone="89197711249",
                 team=t)
    burov.save()