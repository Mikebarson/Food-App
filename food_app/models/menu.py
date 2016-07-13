from django.db import models
from django.utils import timezone
from django.db.models import Q, Count
# from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import math
import copy

from ..models.restaurant import *
from ..models.food import *

class Menu_category(models.Model):
	restaurant = models.ForeignKey("Restaurant")
	is_deleted = models.BooleanField(default=False)
	# company       = models.ForeignKey("User_company")
	# created_by    = models.ForeignKey("User")
	class Meta:
		app_label = "food_app"
		db_table  = "menu_category"

class Menu_category_details(models.Model):
	name = models.CharField(max_length=100)
	menu_category = models.ForeignKey("Menu_category")
	description = models.CharField(max_length=300)
	is_deleted = models.BooleanField(default=False)
	# company       = models.ForeignKey("User_company")
	# created_by    = models.ForeignKey("User")
	class Meta:
		app_label = "food_app"
		db_table  = "menu_category_details"
