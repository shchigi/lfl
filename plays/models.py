# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.

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
    start_date = models.DateField(auto_now=False, )
    finish_date = models.DateField(auto_now=False)
    cell_phone = models.CharField(max_length=12)
    email = models.EmailField()

    def clean(self):
        cell_phone_template = "(([+]7)|8)\d{10}"
        if not (re.match(cell_phone_template, self.cell_phone)):
            raise ValidationError("Invalid cell phone format: %s" % self.cell_phone)
