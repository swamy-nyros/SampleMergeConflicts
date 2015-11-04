"use strict";

var app = angular.module("myApp", ['ngResource',"ui.bootstrap"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

app.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/car_index.html",
                                
        })
        .when("/compare_cars", {
            templateUrl: "static/js/app/views/view.html",
            
        })
        .otherwise({
            redirectTo: '/'
        })
})
         

app.factory('MakeDetailService',['$resource',
	function($resource){
		return $resource('api/',{},{
			query:{method:'GET', params:{},isArray:true}
		});
	}
]);

app.controller("myController", function($scope,$http,MakeDetailService)
 	{ 
 	
   		$scope.makeList = MakeDetailService.query();
   		console.log($scope.makeList)

   	 // 	$scope.images=[{id:32,title:"Inglourious Basterds",year:"2009",rating:"6K",comments:"55",queue:"454",review:"Great film, great cast, some amazing stand out scenes. Really liked it."},
     //                 {id:33,title:"Django Unchained",year:"2012",rating:"4K",comments:"163",queue:"704",review:"Imaginative, smart, entertaining and never boring "},
     //                 {id:34,title:"The Hunger",year:"2013",rating:"1K",comments:"70",queue:"147",review:"Simply awesome! And Christoph Waltz earned his Oscar for sure! "},
     //                 {id:35,title:"Pulp Fiction ",year:"1994",rating:"13K",comments:"188",queue:"1K",review:"A good fiction and an aliter end for the Nazis!!"},
     //                 {id:36,title:"Reservoir Dogs",year:"1992",rating:"4K",comments:"55",queue:"888",review:"Classic Tarentino "},
     //                 {id:37,title:"THE EXORICIST",year:"1973",rating:"1K",comments:"19",queue:"138",review:"Excellent film. Cool characters and lots of violence. "},
     //                 {id:38,title:"Star Trek Into Darkness",year:"2013",rating:"583",comments:"73",queue:"265",review:"A retake of the Nazi history Quentin Tarantino style. "},
     //                 {id:39,title:"Silver Linings Playbook",year:"2012",rating:"2K",comments:"115",queue:"442",review:"Very entertaining, great acting, ultra-violent (Tarantino, duh). Perfect."}
     //                 ];

    	// console.log($scope.images)
     

   
} );
    
    
 
 
 
 