angular.module('food_app', ['main_services', 'ngMaterial', 'ngMessages', 'material.svgAssetsCache'])
.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $interpolateProvider.startSymbol('{$').endSymbol('$}');
}])

.controller('food_controller', function($http,$scope,$mdDialog,HttpRequest,$timeout, $mdSidenav, $log){
	$scope.isSidenavOpen = false;
	$scope.openLeftMenu = function(){
		$mdSidenav('left').toggle();
	};
	$scope.read_food = function(){
		$scope.food_list = 
		[
			{'restaurant_name' : 'Ramente', 'food_name' : 'Sushi', 'food_type' : 'Fish', 'price' : 2, 'description':'fresh uncooked fish', 'food_code' : 'RMA142'},
			{'restaurant_name' : 'Ramente', 'food_name' : 'Noodles', 'food_type' : 'Rice', 'price' : 3, 'description':'fresh noodles', 'food_code' : 'RMA1445'},
			{'restaurant_name' : 'Ramente', 'food_name' : 'Shrimp Chips', 'food_type' : 'Junk Food', 'price' : 2.50, 'description':'nice cooked chips', 'food_code' : 'RMA090'},
			{'restaurant_name' : 'Ramente', 'food_name' : 'Salads', 'food_type' : 'Salad', 'price' : 4.50, 'description':'fresh organic salads', 'food_code' : 'RMA02090'},
		];
		
	};

})