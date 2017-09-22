/**
 * Created by tngblt on 12/02/17.
 */
var clickedButton = 0;

$(".button-genre").click( function () {
    var txt= $(this).data("type");

    if($(this).hasClass("clicked"))
    {
        $(this).css('color',$(this).css('background-color'));
        $(this).css('background','transparent');
        $(this).removeClass("clicked");
        $("#genre"+clickedButton).val(null);
        clickedButton--;
    }
    else if(clickedButton < 3)
    {
        $(this).css('background-color',$(this).css('color'));
        $(this).css('color','white');
        clickedButton++;
        $(this).addClass("clicked");

        $("#genre"+clickedButton).val(txt);
    }

        var buttonCreate = $(".buttonCreate");
    if(clickedButton == 0)
    {
        buttonCreate.prop('disabled',true);
        buttonCreate.attr('title',"Veuillez choisir au moins 1 genre musical au dessus.");
    }
    else
    {
        buttonCreate.prop('disabled',false);
        buttonCreate.attr('title',"");
    }

});




$(".button-more").click( function () {
    if ($(this).hasClass("more-clicked"))
    {
        $(".button-genre.more").slideUp();
        $(this).text("Plus de genre");
        $(this).removeClass("more-clicked");
    }
    else {
        // $(".button-genre.more").css('display','inline-flex');
        $(".button-genre.more").slideDown();
        $(this).addClass("more-clicked");
        $(this).text("Moins de genre");
    }

});

$('.rangeIn').on("change mousemove", function () {

    $(this).parent().children('ul.row-label').children('li.my-value').text($(this).val());

});


$('.row').hover( function () {
    $(this).next('.advise').fadeTo(700,1);
}, function () {
    $(this).next('.advise').fadeTo(1500,0);
});
