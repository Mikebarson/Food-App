from django.conf.urls import url, handler404
from food_app.views import home, food, restaurants, menus

urlpatterns = [
	################ HOME FUNCTIONS ################
	url(r'^$', home.show_home, name='show_home'),

	############### FOOD FUNCTIONS #################
	url(r'^food/$', food.show_food, name='show_food'),

	############### RESTAURANT FUNCTIONS #################
	url(r'^restaurants/$', restaurants.show_restaurants, name='show_restaurants'),
	url(r'^restaurants/restaurant_dialog/$', restaurants.restaurant_dialog, name='restaurant_dialog'),
	url(r'^restaurants/save_restaurant/$', restaurants.save_restaurant, name='save_restaurant'),
	url(r'^restaurants/read_all_restaurants/$', restaurants.read_all_restaurants, name='read_all_restaurants'),
	url(r'^restaurants/get_restaurant_types/$', restaurants.get_restaurant_types, name='get_restaurant_types'),
	url(r'^restaurants/menu_dialog/$', restaurants.menu_dialog, name='menu_dialog'),

	###################### MENU FUNCTIONS ######################
	url(r'^menus/$', menus.show_menus, name='show_menus'),
	url(r'^menus/menu_dialog/$', menus.menu_dialog, name='menu_dialog'),
	url(r'^menus/add_menu_category/$', menus.add_menu_category, name='add_menu_category'),
	url(r'^menus/delete_menu_category/(?P<menu_category_details_pk>[0-9]+)$', menus.delete_menu_category, name='delete_menu_category'),
	url(r'^menus/read_all_menu_categories/(?P<restaurant_id>[0-9]+)$', menus.read_all_menu_categories, name='read_all_menu_categories'),
	url(r'^menus/read_menu_category/(?P<menu_category_details_pk>[0-9]+)$', menus.read_menu_category, name='read_menu_category'),

]
