from django import forms
from . models import Survey
from django.db import models
from . data import CHOICES, SLEEP_TIME, WAKE_TIME

class SurveyCreateForm(forms.ModelForm):

    

    class Meta:
        model = Survey
        fields = ('full_name', 'email', 'country','campus','gender', 'year',
                  'scale1','scale2','scale3','scale4','scale5','scale6','scale7','scale8',
                  'extra1','extra2','extra3','extra4','extra5','extra6', 'want_roommate', 'email_roommate' 
        )
