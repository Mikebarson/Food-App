angular.module('restaurant_app', ['main_services', 'ngMaterial', 'ngMessages', 'material.svgAssetsCache','ui-notification', 'ui.bootstrap'])
.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $interpolateProvider.startSymbol('{$').endSymbol('$}');
}])

.controller('restaurant_controller', function($http,$scope,$mdDialog,HttpRequest,$timeout, $mdSidenav, $log, $mdMedia, Notification, $q){
  $scope.isSidenavOpen = false;

  $scope.openLeftMenu = function(){
		$mdSidenav('left').toggle();
	};

  $scope.search_instantiate = function($element){
       $element.find('input').on('keydown', function(ev) {
         ev.stopPropagation();
       });
  }

  $scope.read_all_restaurants  = function(){
    $http.post('/restaurants/read_all_restaurants/')
    .success(function(response){
      $scope.restaurant_list = response;
    })
  }

  $scope.restaurant = {}
  $scope.selected = {}

  $scope.load_menu_list = function(restaurant){
    $scope.restaurant_id = restaurant.id;
  }

  $scope.read_all_menu_categories  = function(data){
    $scope.selected['restaurant'] = data; // we did this so that restaurant can be used any where here without having to specify its id

    $http.post('/menus/read_all_menu_categories/'+data.id)
    .success(function(response){
      if(response == false){ // this means that we found no data on menu categories
        $scope.menu_categories = []
      }else{
        $scope.menu_categories = response.values;
      }
    })
  }

  $scope.read_menu_category  = function(data){
    $http.post('/menus/read_menu_category/'+data.id)
    .success(function(response){
      $scope.dialog_title = 'Edit Menu Category'
      $scope.menu_category_dialog();
      $scope.data = response.values[0];
    })
  }

  $scope.add_menu_category = function(data) {
    $scope.restaurant['name'] = data.name;
    $scope.restaurant['description'] = data.description;
    $scope.restaurant['restaurant'] = data.restaurant.id;
    
    if(data.id != null)
      $scope.restaurant['menu_category_details_id'] = data.id
    
    $http.post('/menus/add_menu_category/', $scope.restaurant)
    .success(function(response){
      Notification.success(response)
      $scope.cancel();
      $scope.read_all_menu_categories(data.restaurant)
    })
    .error(function(err){
      Notification.error(err)
    })
  }

  $scope.add_menu_category_dialog = function($event){
    $scope.data = {}
    $scope.dialog_title = 'Add Menu Category'
    $scope.menu_category_dialog()
  }

  $scope.menu_category_dialog = function($event){
    var useFullScreen = ($mdMedia('sm') || $mdMedia('xs'))  && $scope.customFullscreen;
    $mdDialog.show({
      scope : $scope.$new(),
      templateUrl: 'menu_dialog/',
      parent: angular.element(document.body),
      targetEvent: $event,
      clickOutsideToClose:false,
      fullscreen: useFullScreen
    })
  }

  $scope.delete_menu_category = function(data){
    if(data)
      var ask_user = confirm("Are you sure you want to delete this menu category? You won't be able to take it back!")

    if(ask_user == true)
      $http.post('/menus/delete_menu_category/'+data.id)
      .success(function(response){
        Notification.success(response)
        $scope.read_all_menu_categories($scope.selected['restaurant'])
      })
      .error(function(err){
        Notification.error(err)
      })
  }

  $scope.cancel = function() {
	    $mdDialog.cancel();
	}

})
