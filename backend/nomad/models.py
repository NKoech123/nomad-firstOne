from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    geolocation = models.CharField(max_length=200)
    businessCategoryID = models.ForeignKey('BusinessCategory', on_delete=models.CASCADE,null=False)
    global_score = models.IntegerField()
    friends_score = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class BusinessCategory(models.Model):
    name = models.CharField(max_length=200)

class Schedule(models.Model):
    schedules = ArrayField(models.CharField(max_length=200), blank=True)

class VendorFollowing(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE,null=False, blank=True )
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE,null=False, blank=True )

# class UserFriends(models.Model):
#     user = models.ForeignKey('User', on_delete=models.CASCADE,null=False, blank=True )
#     user = models.ForeignKey('User', on_delete=models.CASCADE,null=False, blank=True )