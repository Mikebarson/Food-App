from django import forms
from ..models.menu import *
from django.contrib.auth import hashers 
from django.utils import timezone

class Menu_category_form(forms.ModelForm):
	class Meta:
		model = Menu_category
		fields = ('restaurant', 'is_deleted')

class Menu_category_details_form(forms.ModelForm):
	class Meta:
		model = Menu_category_details
		fields = ('name', 'menu_category', 'description')