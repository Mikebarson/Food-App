from django import forms
from ..models.restaurant import *
from django.contrib.auth import hashers 
from django.utils import timezone

class Restaurant_form(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ('name','address','location','pin_code', 'landmark', 'phone_no', 'user_email', 'features', 'tags', 'cuisines',
			'timings', 'details', 'review', 'opening_status', 'restaurant_type', 'restaurant_email', 'restaurant_website', 'social_media_sites', 'is_deleted')