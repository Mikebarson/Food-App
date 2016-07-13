angular.module('restaurant_app', ['main_services', 'ngMaterial', 'ngMessages', 'material.svgAssetsCache','ui-notification', 'ui.bootstrap'])
.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $interpolateProvider.startSymbol('{$').endSymbol('$}');
}])

.controller('restaurant_controller', function($http,$scope,$mdDialog,HttpRequest,$timeout, $mdSidenav, $log, $mdMedia, Notification, $q){
	$scope.isSidenavOpen = false;

	$scope.data = {}
	$scope.cuisine_list = ['Soup']
	$scope.feature_list = ['Soup Latte']
	$scope.tag_list = ['#Restaurant']

	$scope.openLeftMenu = function(){
		$mdSidenav('left').toggle();
	};

	$scope.menu_choices =
	[
	   { name: "Add Restaurant", icon: "add_box", direction: "bottom", "id" : "add"},
	   { name: "Delete Mode", icon: "delete", direction: "bottom", "id" : "delete" },
	]

	$scope.restaurant_dialog = function($event, restaurant){
		  var useFullScreen = ($mdMedia('sm') || $mdMedia('xs'))  && $scope.customFullscreen;
      if(restaurant){
  		  $http.post("/restaurants/read_all_restaurants/", restaurant)
  		  .success(function(response){
          $scope.data = response[0];
  		  })
      }

		  $mdDialog.show({
		    scope : $scope.$new(),
		    templateUrl: 'restaurant_dialog/',
		    parent: angular.element(document.body),
		    targetEvent: $event,
		    clickOutsideToClose:false,
		    fullscreen: useFullScreen
		  })
	}

  $scope.menu_dialog = function($event, restaurant){
    var useFullScreen = ($mdMedia('sm') || $mdMedia('xs'))  && $scope.customFullscreen;

    if(restaurant){
      $http.post("/restaurants/read_all_restaurants/", restaurant)
      .success(function(response){
        $scope.data = response[0];
      })
    }

    $mdDialog.show({
      scope : $scope.$new(),
      templateUrl: 'menu_dialog/',
      parent: angular.element(document.body),
      targetEvent: $event,
      clickOutsideToClose:false,
      fullscreen: useFullScreen
    })
  }

	$scope.cancel = function() {
	    $mdDialog.cancel();
	}

	$scope.read_all_restaurants = function(){
		$scope.restaurant_list = []
		$http.post('/restaurants/read_all_restaurants/')
		.success(function(results){
				$scope.restaurant_list = results;
		})
		.error(function(err){
			Notification.error(err)
		})
	};

	$scope.add_restaurant = function(data){
		data['cuisines'] = $scope.cuisine_list
		data['features'] = $scope.feature_list
		data['tags'] = $scope.tag_list
		$http.post('/restaurants/save_restaurant/', data)
		.success(function(results){
			Notification.success('Success');
			$scope.read_all_restaurants()
		})
		.error(function(err){
			Notification.error(err)
		})
	}

	$scope.transform = function(chip){
		return {
			name : $scope.data.cuisines
		}
	}

	$scope.get_restaurant_types = function(){
		$http.post('/restaurants/get_restaurant_types/')
		.success(function(response){
			$scope.restaurant_types = []
			$scope.restaurant_types.push(response)
		})
		.error(function(err){
			console.log(err)
		})

	}

})
