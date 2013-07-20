momentum = angular.module "Momentum.controllers", []

momentum.controller "PostStudentDetails", ['$scope', '$http', ($scope, $http) ->
	$http.get("/api/poststudentdetails").success (response) ->
		programids = response.progids
		programnames = response.prognames
		$scope.programs = []
		programList = []
		i = 0
		while i <= response.progids.length-1
			programList.push { progids:programids[i], prognames:programnames[i] }
			i++
		$scope.programs = programList;
	.error (response) ->
		alert "Error!"
]
