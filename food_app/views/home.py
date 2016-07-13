from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.db import IntegrityError
import math
import csv
import json

def show_home(request):
	return render(request, 'food_app/home.html')
