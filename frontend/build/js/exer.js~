function donationCtrl($scope) {
    $scope.supporters = 0;
    $scope.goal = 1000000;
    $scope.donations = [
        {name:'Elijah Joshua Cayabyab', amount:1000},
        {name:'Jose Rizal', amount:422323}];
    $scope.comments = [
        'Yeah, this startup is awesome!',
        'No, this sucks...'];
    
    $scope.support = function() {
       $scope.supporters += 1; 
    };

    $scope.donate = function() {
       $scope.addDonations(); 
    };

    $scope.addDonations = function() {
       $scope.donations.push({name:'Random Person', amount:80000});
       $scope.donorName = '';
       $scope.donationAmount = '';
       alert("Thank you! Your donation has been recorded.");
    };

    $scope.getSupporters = function() {
       return $scope.supporters;
    };

    $scope.getTotalDonations = function() {
        var totalDonations = 0;
           angular.forEach($scope.donations, function(donation) {
               totalDonations += donation.amount;
           });
        return totalDonations;
    };
}
