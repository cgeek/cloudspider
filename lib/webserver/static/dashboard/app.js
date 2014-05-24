window.API = {
	signin: 	'/account/sign',
	register: 	'/account/register',
};

window.TemplateUrl = {
	container:'/static/dashboard/partials/container.html',
	dashboard: '/static/dashboard/partials/dashboard/dashboard.html',
	login: '/static/dahsboard/partials/login.html',
};

angular.module('dashboard.routers', []).config(["$stateProvider", "$urlRouterProvider", function($stateProvider,   $urlRouterProvider){
	$stateProvider.state('/dashboard', {
		templateUrl: TemplateUrl.container
	});
}]),

angular.module("dashboard.controllers", [])
.controller("authCtrl", ["$http", "$rootScope", "$scope", "$state",
	function ($http, $rootScope, $scope, $state) {
		$scope.auth = function () {
			!$scope.username && auth_form.username.value && ($scope.username = auth_form.username.value), !$scope.password && auth_form.password.value && ($scope.password = auth_form.password.value), 
			$http.post(API.signin, {
				username: $scope.username,
				password: $scope.password
			}).success(function (result) {
				result.code == 200 ? ($scope.showErrorTip = !1 , $rootScope.userInfo = angular.copy(result.data), $state.go("dashboard.mainpage"))
				:	($scope.error_tip = '用户名或密码错误，请重试', $scope.showErrorTip = !0);
			})
		}
	}
])
.controller('controlPanelCtrl', ["$filter", "$http", "$location", "$log",  "$rootScope", "$scope", "$state", "$stateParams",
	function (e, t, n, r, a, i, o, s, l) {
	
	}
])
.controller('dashboardCtrl', ["$filter", "$http", "$rootScope", "$scope", "$state", "$stateParams", "$modal", "$timeout",
	function($filter, $http, $rootScope, $scope, $state, $stateParams, $modal, $timeout) {
		$rootScope.$watch("inquiry", function($filter) {
			$filter ? console.log($filter) : $http.get(API.inquiryList).success(function(result){
				var t = result.data;
				$rootScope.inquirys = t;
			});
		}),
		$scope.createBucket = function(){
			$modal.open({
				templateUrl: "/assets/partner/partials/_menu/_modal_create_bucket.html",
				controller: "_modalCreateNewInquiryCtrl",
				backdrop: "static"
			});
		};
		$scope.updateRemark = function(data, id) {
			return $http.post('/partners/inquiry/update', {id:id, remark: data});
		};
		$scope.updateAvailable = function(available, inquiry, idx) {
			$scope.inquirys[idx].available = available;
			return $http.post('/partners/inquiry/update', {id:inquiry.id, available: available});
		};
		var poll = function() {
			$timeout(function() {
				$http.post('/partners/inquiry/partnerUnread', {last_id: $scope.inquirys[0].id}).success(function(result){
					if(result.code == 200 && result.data.new_count && result.data.new_count > 0) {
						for(var i =0; i < result.data.inquiry_list.length; i++) {
							$scope.inquirys.splice(0, 0, result.data.inquiry_list[i]);
						}
						document.title='【有新询单】';
					}
				});
				poll();
			}, 10 * 1 * 1000);
		};     
		poll();
	}
])
.controller("_modalCreateNewInquiryCtrl", ["$http", "$modalInstance", "$rootScope", "$scope", "$state",
	function ($http, $modalInstance, $rootScope, $scope, $state) {
		$scope.submit = function() {
			$http.post("/partners/inquiry/create", {content:$scope.content}).success(function(result) {
				if(result.code == 200) {
				   	$modalInstance.close();
					$scope.inquirys.splice(0, 0, result.data);
				} else { 
					alert(result.message) 
				}
			});
		},
		$scope.skip = function(){
			$modalInstance.close('cancel');
		};
	}
]);

angular.module('cloudSpider.services', []);

angular.module('cloudSpider',[
	'ui.router',
	'dashboard.routers',
	'dashboard.controllers',
	'cloudSpider.services'
])
.run(["$http", "$location", function($http, $location) {
	console.info("CloudSpider[ " + CloudSpider.app._version + "]Super!!!");
}]);
