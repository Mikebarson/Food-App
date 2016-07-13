angular.module('home_app', ['main_services', 'ngMaterial', 'ngMessages', 'material.svgAssetsCache'])
.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $interpolateProvider.startSymbol('{$').endSymbol('$}');
}])
.controller('home_controller', function($http,$scope,$mdDialog,HttpRequest,$timeout, $mdSidenav, $log){

	$scope.isSidenavOpen = false;
	$scope.openLeftMenu = function(){
	  $mdSidenav('left').toggle();
	};
  
	// $scope.$watch('isSidenavOpen', function(isSidenavOpen) {
	//     alert('sidenav is ' + (isSidenavOpen ? 'open' : 'closed'));
	// });

})
