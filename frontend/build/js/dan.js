(function() {
  var momentum;

  momentum = angular.module("Momentum.controllers", []);

  momentum.controller("DanController", [
    '$scope', '$http', function($scope, $http) {
      return $scope.postScholarship = function() {
        return $http.post("/api/postscholarship", {
          title: $scope.data.title,
          description: $scope.data.description
        }).success(function(response) {
          return alert("Success!");
        }).error(function(response) {
          return alert("Failure!");
        });
      };
    }
  ]);

}).call(this);
