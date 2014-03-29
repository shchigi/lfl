__author__ = 'rakot'
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from plays.models import Match, Goal

@receiver(pre_save, sender=Match)
def check_goals_in_match(sender, instance, *args, **kwargs):
    print "check_goals_in_match is here"
    print instance
    goals = Goal.objects.filter(match=instance)
    home_team_score = guest_team_score = 0
    for goal in goals:
        isHomeT = (goal.player_scored.team == instance.home_team)
        if isHomeT == goal.own_goal:
            guest_team_score += 1
        else:
            home_team_score += 1
    if not (guest_team_score == instance.guest_team_score and home_team_score == instance.home_team_score):
        raise ValidationError(u"Error while updating match pk=%d. Please check up matches in database" % instance.pk)
    print "OK"
