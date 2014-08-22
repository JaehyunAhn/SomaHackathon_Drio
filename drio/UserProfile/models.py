from django.db import models, IntegrityError
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import date


class UserProfile(models.Model):
    # User basic inherits : username, password, email
    user = models.OneToOneField(User)
    # Profile information
    nickname = models.CharField(max_length=63)
    birth = models.DateField(null=True) # TODO change null = false
    gender = models.CharField(max_length=15, null=False)
    genderPreference = models.CharField(max_length=15, null=False)
    description = models.TextField(blank=True, null=True)
    hobby = TaggableManager()
    email = models.EmailField(max_length=254)

    region = models.CharField(max_length=63, null=True)
	# ImageField: http://goo.gl/ZQEG4e
    avatar = models.ImageField(upload_to='/avatar/')
    # Foreign Keys : taggit Django

    # specification
    height = models.PositiveSmallIntegerField(null=False)
    jobArea = models.TextField(blank=True, null=True)
    jobDesc = models.TextField(max_length=63)
    salary = models.PositiveSmallIntegerField(null=False)
    home = models.TextField(null=False)
    car = models.TextField(null=False)

    class Meta:
        unique_together=('nickname','user')

class Evaluation(models.Model):
    toUser = models.ForeignKey(User, related_name='evaluation_request_received')
    fromUser = models.ForeignKey(User, related_name='evaluation_request_sent')
    stars = models.FloatField(blank=False)
    desc = models.TextField(max_length=254)

class UserPreference(models.Model):
    user = models.OneToOneField(User)
    hobby = TaggableManager()
    noField = models.TextField(blank=False)
    noSpecific = models.TextField(blank=False)
    yesField = models.TextField(blank=False)
    yesSpecific = models.TextField(blank=False)

class Message(models.Model):
    toUser = models.ForeignKey(User, related_name = 'message_request_received')
    fromUser = models.ForeignKey(User, related_name = 'message_request_sent')
    status = models.TextField(max_length=63)
    contents = models.TextField(max_length=254)
