/**
 * Created by Rebecca Hanlon on 5/31/17. Exploring jQuery.
 */


function addToList(item) {
    // add a todo item into the list
    var $listItem = $('<li class="myclass">').text(item);
    var $addX = $('<span class="checkX">').text('X');
    $addX.css();
    $listItem.append($addX);
    $('#list').append($listItem);


    //add check off & line-through



    $listItem.on('click', function(event){

    // event handler for clicking on the list items
    $(this).css("text-decoration', line-through");
    });


}


$('#submit').on('click', function(event) {
    // event handler for handling todo item
    event.preventDefault();
    /* event handler capturing the input */
    var $inputBox = $('#todo').val();
    addToList($inputBox);
});





