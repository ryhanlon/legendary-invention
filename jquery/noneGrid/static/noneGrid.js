/**
 * Created by Rebecca Hanlon on 6/1/17.
 */


$('.boxes').mouseover(function() {
    // random color generator
    let $red = (Math.floor(Math.random() * 256));
    let $green = (Math.floor(Math.random() * 256));
    let $blue = (Math.floor(Math.random() * 256));

    $(this).css({'background-color': `rgb(${$red}, ${$green}, ${$blue})`}).css('transition', '.5s');

    // match up words, change 'None' to name of box
    let $swap = $(this).text();
    $('#change').text($swap);

});




