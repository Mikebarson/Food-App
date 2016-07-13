from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from random import randint
from django.utils.termcolors import colorize
from django.db.models import Count,Q,F,Sum,Avg,Min
import json
import datetime,time

def extractObj(data):
	try:
		for key in data:
			print(key)
			if isinstance(data[key], dict):
				if 'id' in data[key]:
					data[key] = data[key]['id']
		return data
	except Exception as e:
		print(e)
		
# We get the data which is "ID" and model
def get_name_of_id(data,  models):
	try:
		results = models.objects.filter(id=data).values('name').first()
		return results
	except Exception as err:
		print(err)