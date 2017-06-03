/**
 * Created by Rebecca Hanlon on 6/2/17.
 */





//
// // build badge
// $('#inner-container').append("<div class='badge'><p class='info'>jfjjfjf</p></div>");
//
//
// function addBox($fullName, $email, $userID, $registrationDate, $dateOfBirth  ) {
//     "use strict";
//
//     let $innerContainer = $('#inner-container');
//     let $badge = $('<div class="badge"></div>');
//     let $name = $innerContainer.append(`<p class="info"><strong>name:</strong> ${$title} ${firstName} ${lastName}</p>`);
//
// //     let $emailFormat = $innerContainer.append(`<p class="info"><strong>email:</strong> ${$email}</p>`);
// //     let $userFormat = $innerContainer.append(`<p class="info"><strong>user:</strong> ${$userID}</p>`);
// //     $innerContainer.append($badge);
// }
//
// // accessing for information
// function accessData(data) {
//     "use strict";
//     $.each(data.results, function(index, user){
//
//     let $title = user.name.title;
//     let $firstName = user.name.first;
//     let $lastName = user.name.last;
//     let $fullName = $title + $firstName + $lastName;
//
//     let $email = user.email;
//     let $userID = user.login.username;
//     let $registrationDate = user.registered;
//     let $dateOfBirth = user.dob;
//
//     addBox($fullName, $email, $userID, $registrationDate, $dateOfBirth);
//     });
// }
//
//
// // retrieve the data
// function fetchData() {
//     "use strict";
//
//     let data;
//
//     $.ajax({
//         url: 'https://api.randomuser.me',
//         method: 'GET',
//         data: {'results': 5},
//         success: function(rsp){
//             "use strict";
//             console.log(rsp);
//             data = rsp;
//             accessData(data);
//         },
//         error: function(err){
//             "use strict";
//             console.log(err);
//         }
//     });
// }


$('button').on('click', function() {
    console.log('started');
    // fetchData();
});
//
// $('#generate').hide();

