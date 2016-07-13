from django.db import models
from django.utils import timezone
from django.db.models import Q, Count
# from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import math
import copy

from ..models.restaurant import *
from ..models.menu import *

class Food(models.Model):
	restaurant = models.ForeignKey("Restaurant")
	is_deleted = models.BooleanField(default=False)
	# nutritional_details = models.ForeignKey("Nutrition")
	# company       = models.ForeignKey("User_company")
	# created_by    = models.ForeignKey("User")
	class Meta:
		app_label = "food_app"
		db_table  = "food"

class Food_details(models.Model):
	price = models.FloatField()
	food = models.ForeignKey("Food")
	name = models.CharField(max_length=100)
	food_type = models.ForeignKey("Food_type")
	description = models.CharField(max_length=300)
	menu_category = models.ForeignKey("Menu_category")
	class Meta:
		app_label       = "food_app"
		db_table        = "food_details"

class Food_type(models.Model):
	name = models.CharField(max_length=100)
	restaurant_type = models.ForeignKey("Restaurant_type")
	is_deleted  = models.BooleanField(default=False)
	# company       = models.ForeignKey("User_company")
	# created_by    = models.ForeignKey("User")
	class Meta:
		app_label       = "food_app"
		db_table        = "food_type"
