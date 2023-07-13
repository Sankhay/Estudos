$(document).ready(function() {
    $("#myButton").click(function() {
        $.ajax({
            url: "/rota4",
            type: "GET",
            success: function(response) {
                console.log(response);
            },
            error: function(xhr) {
                console.log("Erro: " + xhr.status);
            }
        });
    });
});
