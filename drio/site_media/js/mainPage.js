'use strict'

$(document).ready(function()
{
    var $login = $('#login');
    var $start = $('#start');
    $('#login_btn').click(function()
    {
        $start.hide();
        $login.css({display:'block', height:0, opacity:0, width:0}).animate({
            height:'250px',
            opacity:1,
            width:'300px'
        }, 500);
    });

    $('#login_close').click(function()
    {
        $start.show();
        $login.hide();
    })
})
