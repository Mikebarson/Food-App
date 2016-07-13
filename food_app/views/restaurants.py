from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.db import IntegrityError
import math
import csv
import json

from ..forms.restaurant_forms import *
from ..models.restaurant import *
from ..views.common import *

def show_restaurants(request):
	form  = Restaurant_form()
	return render(request, 'food_app/restaurant/restaurant_default.html', {'form' : form})

def restaurant_dialog(request):
	return render(request, 'food_app/restaurant/restaurant_dialog.html')

def menu_dialog(request):
	return render(request, 'food_app/menu/menu_dialog.html')

def save_restaurant(request):
	try:
		data = json.loads(request.body.decode("utf-8")) if request.body.decode("utf-8") else {}
		data = extractObj(data)

		try:
			instance = Restaurant.objects.get(name__icontains=data.get('name', None))
			return HttpResponse('Restaurant already exists! Please add a different Restaurant.', status=400)
		except Restaurant.DoesNotExist:
			form = Restaurant_form(data)

		if(form.is_valid()):
			form_pk = form.save()
		else:
			raise ValueError(form.errors)
		return HttpResponse('Success!', status=200)
	except Exception as err:
		print(err)
		return HttpResponse(err, status=400)

def read_all_restaurants(request):
	try:
		rows = []
		data = json.loads(request.body.decode('utf-8')) if request.body.decode("utf-8") else {}
		if data.get('id', None):
			results = Restaurant.objects.filter(id=data.get('id', None)).values()
			for row in results:
				rows.append(row)
		else:
			data = Restaurant.objects.all().values()
			for row in data:
				row['restaurant_type'] = get_name_of_id(row['restaurant_type_id'], Restaurant_type) if row['restaurant_type_id'] else None
				rows.append(row)
		return HttpResponse(json.dumps(rows), status=200)
	except Exception as err:
		print(err)
		return HttpResponse(err, status=400)

def get_restaurant_types(request):
	try:
		query = Restaurant_type.objects.all().values().first()
		print(query)
		return HttpResponse(json.dumps(query), status=200)
	except Exception as err:
		print(err)
		return HttpResponse(err, status=400)
