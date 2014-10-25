__author__ = 'rakot'

from django.contrib import admin
from models import Person, Match, Team, Card, Goal

class PersonAdmin(admin.ModelAdmin):
    pass


class MatchAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


class CardAdmin(admin.ModelAdmin):
    pass


class GoalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Goal, GoalAdmin)