(function() {
  var momentum;

  momentum = angular.module("Momentum.controllers", []);

  momentum.controller("ViewStudentController", [
    '$scope', '$http', function($scope, $http) {
      return $scope.getDetails = function() {
        return $http.get("/api/getstudentdetails/" + $scope.data.personid).success(function(response) {
          $scope.data.lastname = response.split("_")[0];
          $scope.data.degreeprogram = response.split("_")[1];
          $scope.data.reason = response.split("_")[2];
          return alert("asasA");
        }).error(function(response) {
          alert(response);
          return alert("There are no men");
        });
      };
    }
  ]);

}).call(this);
