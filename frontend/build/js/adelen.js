(function() {
  var momentum;

  momentum = angular.module("Momentum.controllers", []);

  momentum.controller("ViewStudentController", [
    '$scope', '$http', function($scope, $http) {
      return $scope.getDetails = function() {
        return alert("asa");
      };
    }
  ]);

}).call(this);
