from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Yelp_Input(models.Model):
    rest1 = models.CharField(max_length=200)
    rest2 = models.CharField(max_length=200)
    rest3 = models.CharField(max_length=200)
    rest4 = models.CharField(max_length=200)
    rest5 = models.CharField(max_length=200)
    choice_text = models.DateTimeField('date published')

    