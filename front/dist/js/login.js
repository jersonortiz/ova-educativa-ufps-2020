$(document).ready(function () {

    var login = $('#loginform');
    var regist = $('#registform');
    var speed = 400;

    $('#to-regist').click(function () {

        $("#loginform").slideUp();
        $("#registform").fadeIn();
    });

    $('#to-login').click(function () {

        $("#registform").hide();
        $("#loginform").fadeIn();
    });

});