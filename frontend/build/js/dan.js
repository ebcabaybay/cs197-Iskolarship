(function() {
  var momentum;

  momentum = angular.module("Momentum.controllers", []);

  momentum.controller("DanController", [
    '$scope', '$http', function($scope, $http) {
      $scope.postScholarship = function() {
        return $http.post("/api/postscholarship", {
          file: $scope.data.file,
          title: $scope.data.title,
          description: $scope.data.description
        }).success(function(response) {
          return alert("Success!");
        }).error(function(response) {
          return alert("Failure!");
        });
      };
      return $(function() {
        $('#degree_cb').change(function() {
          return $('#degree_choice').toggle();
        });
        $('#gender_cb').change(function() {
          return $('.gc').toggle();
        });
        $('#year_cb').change(function() {
          return $('#year_choice').toggle();
        });
        $('#income_cb').change(function() {
          return $('#income_choice').toggle();
        });
        return $('#income_input').keyup(function() {
          var value;

          value = document.getElementById('income_input').value;
          if (!isNaN(parseInt(value, 10)) && parseInt(value, 10) > 0) {
            document.getElementById('income_input').value = parseInt(value, 10);
            return document.getElementById('post-button').disabled = false;
          } else {
            return document.getElementById('post-button').disabled = true;
          }
        });
      });
    }
  ]);

}).call(this);
