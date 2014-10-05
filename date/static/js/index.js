/**
 * Created by johanna on 10/3/14.
 */
$(document).ready(function() {
var url = "";
var form;

 $("button#firstForm").on('click', function() {
        console.log("hELLO");
        getForm("/core_beliefs/");
        console.log(form);
       $("#questions").html("<p>Core Beliefs: </p><form method='post', name='status'>{% csrf_token %}" + "{{ " +  form + ".as_p }}" +
                "<input type='submit' value='Submit'></form>")

    });

var getForm = function (url) {
    console.log("Hello");
    $.ajax({
        url: url,
        dataType: "jsonp",
        type: "GET",
        success: function (data) {
            form = data.form
        },
        error: function (response) {

        }
    });
};

var coreBeliefs = function () {
    var beliefs = $('#beliefs').val();
    console.log("Core Beliefs: " + beliefs);
    var beliefsData = { core_beliefs : beliefs };
    postData = JSON.stringify(beliefsData);
    $.ajax({
        url: '/core_beliefs/',
        type: 'POST',
        dataType: 'json',
        data: postData,
        success: function (response) {
            console.log(response);

            $("#questions").html("<form method='post', name='status'>{% csrf_token %}"+ "{{" + form+ ".as_p }}" +
                "<input type='submit' value='Status'></form>")
        }
    })
}
});