# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
import re


class Team(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Match(models.Model):
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    home_team = models.ForeignKey(Team, related_name="home_team")
    guest_team = models.ForeignKey(Team, related_name="guest_team")
    home_team_scored = models.IntegerField(null=True, blank=True)
    guest_team_scored = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        match_name = "%s - %s" % (self.home_team.name, self.guest_team.name)
        if self.home_team_scored:
            ht_scored = self.home_team_scored
            gt_scored = self.guest_team_scored
            return unicode(match_name + (" %d : %d" % (ht_scored, gt_scored)))
        return unicode(match_name)


class Person(models.Model):
    GOALKEEPER = 'G'
    BACK = 'B'
    HALFBACK = 'H'
    FORWARD = 'F'
    COACH = 'C'
    POSITION_CHOICES = (
        (GOALKEEPER, 'Вратарь'),
        (BACK, 'Защитник'),
        (HALFBACK, 'Полузащитник'),
        (FORWARD, 'Нападающий'),
        (COACH, 'Тренер'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES)
    is_active = models.BooleanField(default=True)
    is_captain = models.BooleanField(default=False)
    start_date = models.DateField(auto_now=False)
    finish_date = models.DateField(blank=True, null=True)
    cell_phone = models.CharField(max_length=12)
    email = models.EmailField(null=True, blank=True)
    team = models.ForeignKey(Team)
    matches = models.ManyToManyField(Match)

    def clean(self):
        cell_phone_template = "(([+]7)|8)\d{10}"
        if not (re.match(cell_phone_template, self.cell_phone)):
            raise ValidationError("Invalid cell phone format: %s" % self.cell_phone)

    def __unicode__(self):
        return unicode("%(name)s %(sirname)s" % {"name": self.first_name, "sirname": self.last_name})


class Match(models.Model):
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    home_team = models.ForeignKey(Team, related_name="home_team", null=False, blank=False)
    guest_team = models.ForeignKey(Team, related_name="guest_team", null=False, blank=False)


class Goal(models.Model):
    player_scored = models.ForeignKey(Person, null=False, related_name="player_scored")
    player_assisted = models.ForeignKey(Person, null=True, blank=True, related_name="player_assisted")
    own_goal = models.BooleanField(default=False)
    number = models.IntegerField(null=True, blank=True)  #Поле для учета порядка гола (можно указывать минуты,
                                                         #Можно указывать порядковый номер для учета, как шел матч.

class Card (models.Model):
    RED = 'R'
    YELLOW = 'Y'
    CARD_TYPES = (
        (RED, "Красная карточка"),
        (YELLOW, "Желтая карточка"),
    )

    type = models.CharField(max_length=1, choices=CARD_TYPES)
    person = models.ForeignKey(Person, null=False, blank=False)
    number = models.IntegerField(null=True, blank=True)  #Тот же комментарий, что и для такого же поля в классе Goal

