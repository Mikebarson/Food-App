from django.conf.urls import include, url
from django.contrib import admin
from food_app.views import *

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'food_order.views.home', name='home'),

    url('', include('food_app.urls')),
]
