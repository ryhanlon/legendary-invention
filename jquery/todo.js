/**
 * Created by Rebecca Hanlon on 5/31/17.
 */


// $('div').val();

// $('.printout').css('border', '1px solid blue');


function addToList(item) {
    var $listItem = $('<li class="myclass">').text(item);
    $listItem.on('click', function(event){
        // event handler for clicking on the list items
        $(this).css("text-decoration', line-through");
    });
    $('#list').append($listItem);
}


$('#submit').on('click', function(event) {
    // event handler for handling todo item
    event.preventDefault();
    /* event handler capturing the input */
    var $inputBox = $('#todo').val();
    addToList($inputBox);
});





