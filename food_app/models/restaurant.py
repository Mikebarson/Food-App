from django.db import models
from django.utils import timezone
from django.db.models import Q, Count
# from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import math
import copy
from ..models.food import *

class Restaurant(models.Model):
	name          = models.CharField(max_length=100)
	address		  = models.CharField(max_length=100)
	location      = models.CharField(max_length=100)
	pin_code	  = models.CharField(max_length=100)
	landmark	  = models.CharField(max_length=100) # A landmark where the restaurant could be located
	phone_no	  = models.CharField(max_length=100)
	user_email	  = models.CharField(max_length=100)
	features	  = models.CharField(max_length=100) # Features found in the restaurant
	tags		  = models.CharField(max_length=100) # tags - links or hashtags for that restaurant
	cuisines	  = models.CharField(max_length=100) # list of food tyoe items available for that restaurant
	timings 	  = models.CharField(max_length=100) # times at which the restaurant is open
	details		  = models.CharField(max_length=100) # details about the restaurant
	review		  = models.CharField(max_length=100) # review (from customers) of the restaurant
	opening_status  = models.CharField(max_length=100) # current status of the restaurant (open, closed, rennovating, etc.)
	restaurant_type = models.ForeignKey("Restaurant_type") # type of restaurant
	restaurant_email = models.CharField(max_length=100)
	restaurant_website = models.CharField(max_length=100)
	social_media_sites = models.CharField(max_length=100) # socail media sites of restaurant (FB, INSTA, SNAP, TWITTER, TUMBLR, etc.)
	is_deleted    = models.BooleanField(default=False)
	# company       = models.ForeignKey("User_company")
	# created_by    = models.ForeignKey("User")

	class Meta:
		app_label       = "food_app"
		db_table        = "restaurant"

class Restaurant_type(models.Model):
	name = models.CharField(max_length=100)
	is_deleted   = models.BooleanField(default=False)
	# company       = models.ForeignKey("User_company")
	# created_by    = models.ForeignKey("User")
	class Meta:
		app_label       = "food_app"
		db_table        = "restaurant_type"
