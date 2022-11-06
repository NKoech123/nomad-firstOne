from django.db import models

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
