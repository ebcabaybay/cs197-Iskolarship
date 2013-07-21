momentum = angular.module "Momentum.controllers", []

momentum.controller "ViewScholarshipController", ['$scope', '$http', ($scope, $http) ->
	$scope.getDetails = ->
		$http.get("/api/scholarships/#{$scope.data.scholarshipid}")
		.success (response) ->
			$scope.title = response.split("_")[0]
			$scope.description = response.split("_")[1]
			$scope.slots = response.split("_")[2]
			$scope.isactive = response.split("_")[3]
			$scope.sponsor = response.split("_")[4]
		.error (response) ->
			alert response
			alert "There are no scholarship"
]