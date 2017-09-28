indexBody.controller("profile", function($scope){
    $scope.name = "Fei Liang";
    $scope.fields = ["Machine Learing", "Software Engineer"];
    $scope.generateFieldsString = function(){
        var fieldsString = ""
        for (var i = 0; i < $scope.fields.length; i++) {
            fieldsString += $scope.fields[i] + " & ";
        }
        fieldsString = fieldsString.slice(0, -3);
        return fieldsString
    };
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
