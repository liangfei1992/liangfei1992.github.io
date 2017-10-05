indexBody.controller("profile", function($scope, $timeout){

    var name = "Fei Liang";
    $scope.nameToShow = "Hello World !";
    $scope.typeUnfinished = true;
    $scope.textColor = "blue-text";
    var typeDelete = function(){
        if ($scope.nameToShow.length > 0) {
            $scope.nameToShow = $scope.nameToShow.slice(0, -1);
            $timeout(typeDelete, 100);
        } else {
            $scope.textColor = "black-text";
            $timeout(typeAdd, 500);
        }
    };
    var typeAdd = function(){
        if ($scope.nameToShow.length < name.length) {
            $scope.nameToShow = $scope.nameToShow + name.charAt($scope.nameToShow.length);
            $timeout(typeAdd, 100);
        } else {
            $timeout(function(){
                $scope.typeUnfinished = false;
            }, 1000)
        };
    };
    $timeout(typeDelete, 2000);

    $scope.fields = ["Machine Learing", "Software Engineer"];
    $scope.generateFieldsString = function(){
        var fieldsString = ""
        for (var i = 0; i < $scope.fields.length; i++) {
            fieldsString += $scope.fields[i] + " & ";
        }
        fieldsString = fieldsString.slice(0, -3);
        return fieldsString
    };
    $scope.resumes = [
        {
            name: "PDF",
            url: "resources/Fei_Liang_Resume.pdf",
        },
        {
            name: "LinkedIn",
            url: "https://www.linkedin.com/in/fei-liang-69b591130/",
        },
    ];

})

indexBody.controller("contacts",function($scope){
    $scope.contactInfo = {
        "email": "liangfei_job@163.com",
        "call": "+1 (314)-435-5113",
        "web": "https://liangfei1992.github.io/",
        "home": "San Jose",
    };
    $scope.test = {
        "1":"2",
        "3":"4",
    }
})
