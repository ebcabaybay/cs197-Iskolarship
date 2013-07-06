momentum = angular.module "Momentum.controllers", []

momentum.controller "ViewStudentController", ['$scope', '$http', ($scope, $http) ->
	$scope.getDetails = ->
		$http.get("/api/getstudentdetails/#{$scope.data.personid}")
		.success (response) ->
			$scope.data.lastname = response.split("_")[0]
			$scope.data.degreeprogram = response.split("_")[1]
			$scope.data.reason = response.split("_")[2]
			$scope.nameid = response.split("_")[0]
			$scope.degreeprogram = response.split("_")[1]
			$scope.yearlevel = "III - "
			$scope.targetmoney = response.split("_")[3]
			$scope.reason = response.split("_")[2]
		.error (response) ->
			alert response
			alert "There are no men"
		
]
