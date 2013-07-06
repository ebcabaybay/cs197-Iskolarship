(function() {
  var momentum;

  momentum = angular.module("Momentum.controllers", []);

  momentum.controller("ViewStudentController", [
    '$scope', '$http', function($scope, $http) {
      return $scope.getDetails = function() {
        return $http.get("/api/getstudentdetails/" + $scope.data.personid).success(function(response) {
          $scope.data.lastname = response;
          return alert("asasA");
        }).error(function(response) {
          alert(response);
          return alert("There are no men");
        });
      };
    }
  ]);

}).call(this);
