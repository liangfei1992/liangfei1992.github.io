indexBody.controller("aboutme", function($scope){
    $scope.aboutme = [
        "I graduated from Washington University in St. Louis this year (2017)",
        "My major was Computer Science, and I got the certificate in Machine Learning and Data Mining",
        "In my free time I play table tennis and try some new techniques",
        "Currently I am learning more about iOS and angularjs",
        "Life is short, I love Python",
    ]
})

indexBody.controller("projects", function($scope){
    $scope.projects = [
        {
            title: "Machine Learning",
            description: "Machine Learning & Data Mining & Deep Learning",
            imageAddress: "resources/ml.png",
            projects: [
                {
                    name: "Image Classification of Dogs and Cats using Gaussian Process",
                    url: "https://github.com/lfdyf20/SP17-515-Final-Project",
                },
                {
                    name: "Clustering and Classification for Gene Functions",
                    url: "#",
                }
            ]
        },
        {
            title: "Software Development",
            description: "iOS Applications & Video Games",
            imageAddress: "resources/app.png",
            projects: [
                {
                    name: "Rate Y: iOS Application Development",
                    url: "https://github.com/lfdyf20/438-IOS-Development-Project---Rate-Y",
                },
                {
                    name: "MFPS Game Development: Run Joey! Run!",
                    url: "https://github.com/lfdyf20/Run-Joey-Run",
                },
            ]
        },
        {
            title: "Full Stack Web Development",
            description: "Django & HTML & CSS & jQuery",
            imageAddress: "resources/web.png",
            projects: [
                {
                    name: "Star Social: Website Development",
                    url: "#",
                }
            ]
        },
        {
            title: "Big Data and Cloud Computing",
            description: "MapReduce & Spark",
            imageAddress: "resources/bigdata.png",
            projects: [
                {
                    name: "Spam Detection Filter",
                    url: "#",
                },
                {
                    name: "Recommendation System Based on Netflix Rating Dataset",
                    url: "#",
                }
            ]
        }
    ]
})

indexBody.controller("skills", function($scope){
    $scope.skills = [
        {
            skillName: "Programming",
            skills: [
                {
                    skill: "python",
                    percents: "60",
                    color: "bg-danger"
                },
                {
                    skill: "swift",
                    percents: "30",
                    color: "bg-warning"
                },
            ]
        },
        {
            skillName: "Machine Learning",
            skills: [
                {
                    skill: "python",
                    percents: 50,
                    color: "bg-danger",
                },
                {
                    skill: "Matlab",
                    percents: 20,
                    color: "bg-warning",
                },
                {
                    skill: "R",
                    percents: 10,
                    color: "bg-info",
                },
                {
                    skill: "pySpark",
                    percents: 10,
                    color: "bg-success",
                },

            ]
        },
        {
            skillName: "Software & Game Development",
            skills: [
                {
                    skill: "Xcode & Swift",
                    percents: 50,
                    color: "bg-danger",
                },
                {
                    skill: "Unity",
                    percents: 40,
                    color: "bg-warning",
                }
            ]
        },
        {
            skillName: "MapReduce & Spark",
            skills: [
                {
                    skill: "Python & Hadoop Streaming",
                    percents: 40,
                    color: "bg-danger",
                },
                {
                    skill: "pySpark",
                    percents: 20,
                    color: "bg-warning",
                },
                {
                    skill: "MapReduce",
                    percents: 10,
                    color: "bg-info",
                },
            ]
        },
    ]
})
