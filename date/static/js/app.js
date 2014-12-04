var date = angular.module('date', ['ngRoute', 'ngCookies', 'ui.bootstrap']);

date.run(function ($http, $cookies) {
    console.log(csrftoken);
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    $http.defaults.headers.put['X-CSRFToken'] = $cookies['csrftoken'];
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

date.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/js/views/question.html', controller: questionController }).
        otherwise({redirectTo: '/'});
}]);
