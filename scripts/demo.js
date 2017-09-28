var demoBody = angular.module("demoBody", []);
demoBody.controller("demos", function($scope){
    $scope.demoAddress = "resources/demos/";
    $scope.gameDemos = [
        {
            name: "Run Joey! Run!",
            url: $scope.demoAddress + "Run_Joey.mov",
            poster: $scope.demoAddress + "Run Joey Run Cover.png",
        },{
            name: "Glitch Garden",
            url: $scope.demoAddress + "Glitch_Garden_Phil.mp4",
            poster: $scope.demoAddress + "Glitch Garden Cover Image.png"
        },
    ]
    $scope.iosDemos = [
        {
            name: "Rate Y",
            url: $scope.demoAddress + "Rate Y.mov",
            poster: $scope.demoAddress + "Rate Y Cover.png"
        },
    ]

})
