angular.module('main_services', [])

.factory('HttpRequest', function($http){
    return {
        simpleRequest: function(data){
          var url = data.url;
          var data = data.data;
          return $http.post(url,data);
        }
    }
})

.factory('DialogController', function($mdDialog){
    return{
      hide : function() {
        $mdDialog.hide();
      },
      cancel : function() {
        $mdDialog.cancel();
      },
      answer : function(answer) {
        $mdDialog.hide(answer);
      },
    }
})

.factory('Toast', function($mdToast,$http){
  return{
    simple : function(message,delay,position){
      if(!delay)
        delay = 5000;

      if(!position)
        position = 'bottom right';

      $mdToast.show(
        $mdToast.simple()
          .textContent(message)
          .hideDelay(delay)
          .position(position)
      );
    },
  }
})

.factory('Dialogs', function(ngDialog){

  return {
    simpleDialog: function(message){
        return ngDialog.open({
                template: '<h2><i class="glyphicon glyphicon-ok" id="successicon"></i>  ' + message +'</h2>',
                // className: 'dialogNotify',
                plain: true,
                showClose : false
              });
    },
    errorDialog: function(message){
        return ngDialog.open({
                  template: '<h2><i class="glyphicon glyphicon-remove" id="erroricon"></i>  ' + message +'</h2>',
                  plain: true
                });
    },
    cautionDialog: function(message){
        return ngDialog.open({
                  template: '<h2><i class="glyphicon glyphicon-question-sign" id="infoicon"></i>  ' + message +'</h2>',
                  plain: true
                });
    },
    confirmDialog: function(data){
        return ngDialog.openConfirm({
                template: '<div class="ngdialog-message">\
                           <h4>Confirm?</h4>\
                           </div>\
                           <div class="ngdialog-buttons">\
                           <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">Confirm</button>\
                           <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog()")">Cancel</button>\
                           </div>',
            plain: true
        });
    },
    editDialog: function(data){
        return ngDialog.open({  //OPENING THE DIALOG
            template: data.template,
            className: data.classname,
            scope: data.scope,
            showClose : true,
            closeByEscape : true
        });
    }

  };
})