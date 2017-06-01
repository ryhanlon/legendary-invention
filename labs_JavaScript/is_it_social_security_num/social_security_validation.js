/**
 * Created by Rebecca Hanlon on 5/30/17.
 */
/**
 * Added on by Rebecca Hanlon on 5/30/17.
 */




/* ************************* */
/* your javascript goes here */

// inside the function below is where you will
// do your work
// the transform function takes a string as an input
// and print out the result using the `printResult`
// function
// you can add more functions above to keep your
// code clean and readable
function transform(input) {
    if (input) {
        clearError();
        // do some transform of the user's input
        // vvvvvv HERE vvvvvv

        // your stuff HERE

            function sSN() {

                var pattern = /\d{3}-?\d{2}-?\d{4}/;

                enterSSN = prompt("Enter your social security number. >> ");

                var patternTest = pattern.test(enterSSN);

                if (patternTest) {
                    alert("This is a valid Social Security Number.");
                } else {
                    alert("This is not a valid Social Security Number.");
                }
            }
            sSN();



        // ^^^^^^ HERE ^^^^^^
        // when you've done the transform,
        // print the result
        printResult(result);
    }
    else {
        printError('Enter a value');
        focusInput();
    }
}

document.addEventListener('DOMContentLoaded', function (evt) {
    // you can rename the `transform` function
    // above, but if you do, you need to change
    // the name here, too
    setup(transform);
    focusInput();
});

/* ************************************** */
/* do not change anything below this line */

function focusInput() {
    document.querySelector('[name="input"]').focus();
}

function printResult(str) {
    document.getElementById('result').innerHTML = str;
}

function printError(str) {
    var err = document.getElementById('error');
    err.classList.add('error');
    err.innerHTML = str;
}

function clearError() {
    var err = document.getElementById('error');
    err.innerHTML = '';
    err.classList.remove('error');
}

function setup(callback) {
    document.querySelector('form')
        .addEventListener('submit', function (evt) {
            evt.preventDefault();
            var value = document.querySelector('input').value;
            callback(value);
        });
}
