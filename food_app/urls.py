from django.conf.urls import url, handler404
from food_app.views import base

urlpatterns = [
	url(r'^$', base.show_base, name='show_base'),
] 