from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.core.validators import RegexValidator

class User(models.Model):
    USER_TYPE = (
        ('Vendor', 'Vendor'),
        ('Customer', 'Customer'),
    )

    BUSINESS_TYPE = (
        (1, 'Food and Beverages'),
        (2, 'Clothes'),
    )
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200,default = 'emptyForNow')
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default = 'Vendor')
    email = models.EmailField(default = 'emptyForNow')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    photo = models.ImageField(upload_to='ProfilePicture/', default = 'emptyForNow')
    bio = models.CharField(max_length=350, null=True) 
    geolocation = models.CharField(max_length=200, default = 'emptyForNow')
    businessType = models.CharField(max_length=1, default = 1, choices=BUSINESS_TYPE)
    global_score = models.IntegerField(default=0)
    friends_score = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField("self", symmetrical=False, default = 0, blank=True, related_name="user_followers")
    follows = models.ManyToManyField("self", symmetrical=False, default= 0, blank=True, related_name='user_follows')

    def __str__(self):
        return self.name
    
    def followers_number(self):
        return self.followers.count()
    
    def following_number(self):
        return self.follows.count()


class Schedule(models.Model):
    user = models.ForeignKey('User', default=1, on_delete=models.CASCADE,null=False, blank=True )
    schedules = ArrayField(models.CharField(max_length=200), blank=True)


