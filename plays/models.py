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
    home_team = models.ForeignKey(Team, related_name="home_team", null=False, blank=False)
    guest_team = models.ForeignKey(Team, related_name="guest_team", null=False, blank=False)
    home_team_score = models.PositiveSmallIntegerField(null=False, blank=True, default=0)
    guest_team_score = models.PositiveSmallIntegerField(null=False, blank=True,  default=0)

    def __unicode__(self):
        return unicode("%s - %s" % (self.home_team.name, self.guest_team.name))


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
    matches_played = models.ManyToManyField(Match, related_name='matches_played')
    matches_intended = models.ManyToManyField(Match, related_name='matches_intended')

    def clean(self):
        cell_phone_template = "(([+]7)|8)\d{10}"
        if not (re.match(cell_phone_template, self.cell_phone)):
            raise ValidationError("Invalid cell phone format: %s" % self.cell_phone)

    def __unicode__(self):
        return unicode("%(name)s %(sirname)s" % {"name": self.first_name, "sirname": self.last_name})


class Goal(models.Model):
    player_scored = models.ForeignKey(Person, null=False, related_name="player_scored")
    player_assisted = models.ForeignKey(Person, null=True, blank=True, related_name="player_assisted")
    own_goal = models.BooleanField(default=False)
    match = models.ForeignKey(Match, null=False, blank=False)
    minute = models.PositiveSmallIntegerField(null=True, blank=True)
    is_penalty = models.BooleanField(default=False, null=False)

    def __unicode__(self):
        assisted = (" (%s)" % (self.player_assisted.last_name,)) if self.player_assisted else ""
        minute = (", %d'"% self.minute) if self.minute else ""
        own_goal = u" (аг)" if self.own_goal else u""
        return unicode(self.player_scored.last_name + assisted + minute + own_goal)

    def clean(self):

        #check if players play in a match
        if ((not self.player_scored.matches_played.filter(pk=self.match.pk).exists()) or
           (self.player_assisted is not None and not self.player_assisted.matches_played.filter(pk=self.match.pk).exists())):
            raise ValidationError("Players in goal do not participate in match. Please add them.")

        #change score in corresponding match
        if not self.own_goal:
            team_scored = self.player_scored.team
        else:
            player_scored_team = self.player_scored.team
            tmp = [self.match.home_team, self.match.guest_team]
            tmp.remove(player_scored_team)
            team_scored = tmp.pop()
        isHomeTeamScored = (self.match.home_team == team_scored)
        if isHomeTeamScored:
            self.match.home_team_score += 1
        else:
            self.match.guest_team_score += 1
        self.match.save()


class Card (models.Model):
    RED = 'R'
    YELLOW = 'Y'
    CARD_TYPES = (
        (RED, "кк"),
        (YELLOW, "жк"),
    )

    type = models.CharField(max_length=1, choices=CARD_TYPES)
    person = models.ForeignKey(Person, null=False, blank=False)
    minute = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        card_type = unicode(" (%s)" % self.type)
        minute = unicode(", %d'" % self.minute) if self.minute else ""
        return unicode(self.person.last_name + minute + card_type)


