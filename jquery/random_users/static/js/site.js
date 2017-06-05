/**
 * Created by Rebecca Hanlon on 6/2/17.
 */





//
// // build badge
// $('#inner-container').append("<div class='badge'><p class='info'>jfjjfjf</p></div>");


function addBox($fullName, $email, $userID, $registrationDate, $dateOfBirth) {
    "use strict";

    let $innerContainer = $('#inner-container');
    let $badge = $('<div class="badge"></div>');
    let $nameFormat = $badge.append(`<pre class="info"><strong>name: </strong> ${$fullName}</pre>`);

    let $emailFormat = $badge.append(`<pre class="info"><strong>email: </strong> ${$email}</pre>`);
    let $userFormat = $badge.append(`<pre class="info"><strong>user: </strong> ${$userID}</pre>`);
    let $registationFormat = $badge.append(`<pre class="info"><strong>registration date: </strong> ${$registrationDate}</pre>`);
    let $dobFormat = $badge.append(`<pre class="info"><strong>birth date: </strong> ${$dateOfBirth}</pre><hr>`);


    $innerContainer.append($badge).append($nameFormat);
}

// // accessing for information
function accessData(data) {
    "use strict";
    $.each(data.results, function(index, user){

    let $title = user.name.title;
    let $firstName = user.name.first;
    let $lastName = user.name.last;
    let $fullName = $title + ' '+ $firstName  + ' ' + $lastName;

    let $email = user.email;
    let $userID = user.login.username;
    let $registrationDate = user.registered;
    let $dateOfBirth = user.dob;

    addBox($fullName, $email, $userID, $registrationDate, $dateOfBirth);
    });
}


// retrieve the data
function fetchData() {
    "use strict";

    let data;

    $.ajax({
        url: 'https://api.randomuser.me',
        method: 'GET',
        data: {'results': 5},
        success: function(rsp){
            "use strict";
            console.log(rsp);
            data = rsp;
            accessData(data);
        },
        error: function(err){
            "use strict";
            console.log(err);
        }
    });
}

//button to see the users
$('button').on('click', function() {
    console.log('started');
    fetchData();
});
//
// $('#generate').hide();

