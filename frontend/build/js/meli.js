(function() {
  var momentum;

  momentum = angular.module("Momentum.controllers", []);

  momentum.controller("PostStudentDetails", [
    '$scope', '$http', function($scope, $http) {
      $scope.data = {
        personid: ""
      };
      $scope.getStudentDetails = function() {
        alert("in");
        return $http.get("/api/poststudentdetails/" + $scope.data.personid).success(function(response) {
          $scope.data.lastname = response;
          return alert("asasA");
        }).error(function(response) {
          alert(response);
          return alert("There are no men");
        });
      };
      return $scope.postStudentDetails = function() {
        return $http.post("/api/poststudentdetails", {
          lastname: $scope.data.lastname,
          firstname: $scope.data.firstname
        }).success(function(response) {
          return alert("Success!");
        }).error(function(response) {
          return alert("Fail!");
        });
      };
    }
  ]);

}).call(this);
