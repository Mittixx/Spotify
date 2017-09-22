/**
 * Created by tngblt on 20/03/17.
 */

var isPlaying = false;

$(".album-preview").click( function () {
    var audio = $(this).children(".audio-player");
    if (audio.hasClass("audio-player") && !audio.hasClass('playing') && !isPlaying)
    {
        audio.get(0).volume = 0.7;
        audio.get(0).play();
        isPlaying = true;
        audio.addClass('playing');
    }
    else if(audio.hasClass('playing'))
    {
        audio.get(0).pause();
        isPlaying = false;
        audio.removeClass('playing');
    }
});

$('')
