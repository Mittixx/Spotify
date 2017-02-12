/**
 * Created by tngblt on 12/02/17.
 */
var clickedButton = 0;

$(".button-genre").click( function () {
    if($(this).hasClass("clicked"))
    {
        $(this).css('color',$(this).css('background-color'));
        $(this).css('background','transparent');
        $(this).removeClass("clicked");
        clickedButton--;
    }
    else if(clickedButton < 3)
    {
        $(this).css('background-color',$(this).css('color'));
        $(this).css('color','white');
        clickedButton++;
        $(this).addClass("clicked");
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

$('.rangeIn').change( function() {
    alert($(this).val());
    $(this).closest('.my-value').text($(this).val());
});
