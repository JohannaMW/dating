$(document).ready(function() {
    var query;

    $("#searchSubmit").on('click', function() {
        getResults();
    });

    var getResults = function () {
        query = $('#search_query').val();
        console.log(query);
    $.ajax({
        url: '/search_singles/' + query + '/',
        type: 'GET',
        success: function (data) {
            $(".resultBlock").html(data);
            console.log(data);
            }
        });
     };

  });
