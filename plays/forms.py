from django.forms import ModelForm
from plays.models import Person

__author__ = 'rakot'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name',
                  'last_name',
                  'position',
                  'cell_phone',
                  'email']