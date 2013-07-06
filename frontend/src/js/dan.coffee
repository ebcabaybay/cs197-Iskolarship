momentum = angular.module "Momentum.controllers", []

momentum.controller "DanController", ['$scope', '$http', ($scope, $http) ->

	$scope.postScholarship = ->
		#alert($scope.data.description)
		$http.post("/api/postscholarship",
			title: $scope.data.title,
			description: $scope.data.description).success (response) ->
				alert "Success!"
			.error (response) ->
				alert "Failure!"
]
		
