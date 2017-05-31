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

      message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
     oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."

      var encoded = input.toLowerCase();

      var alphabet = "abcdefghijklmnopqrstuvwxyz,.- ";  // make the alphabet
      var cesar13 = "nopqrstuvwxyzabcdefghijklm,.- ";   // make coded alphabet

      var decoded = [];  // initialized the array

      for (var i = 0; i < encoded.length; i++) {    // start the for loop, initalize, length, counter
          var enchar = encoded[i];     // index of the encoded message (input)
          var encloc = cesar13.indexOf(enchar); // match the message index to the cesar13
          var decodedChar = alphabet[encloc];  // match the cesar13 index to the alphabet index
          decoded.push(decodedChar);  // add the letter to the array
      }

      var result = decoded.join('');





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
