(function() {
  var momentum;

  momentum = angular.module("Momentum", ["Momentum.controllers", "Momentum.directives"]);

  momentum.config([
    "$routeProvider", function($routeProvider) {
      $routeProvider.when("/post-scholarship", {
        templateUrl: "/html/dan.html",
        controller: 'DanController'
      });
      $routeProvider.when("/post-studentdetails", {
        templateUrl: "/html/post-studentdetails.html",
        controller: 'PostStudentDetails'
      });
      $routeProvider.when("/view-scholarships", {
        templateUrl: "/html/view-scholarships.html",
        controller: 'MessageController'
      });
      $routeProvider.when("/view-studentdetails", {
        templateUrl: "/html/view-studentdetails.html",
        controller: 'MessageController'
      });
      $routeProvider.when("/home", {
        templateUrl: "/html/home.html",
        controller: 'MessageController'
      });
      $routeProvider.when("/404", {
        templateUrl: "/html/404.html"
      });
      $routeProvider.when("/", {
        redirectTo: "/home"
      });
      $routeProvider.when("", {
        redirectTo: "/home"
      });
      return $routeProvider.otherwise({
        redirectTo: "/404"
      });
    }
  ]);

}).call(this);
