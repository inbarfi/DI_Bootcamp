////////////Todo: Bonus - while loop - continue asking for a valid number.

// // If the user guessed more than 3 times, alert "out of chances" and exit the function.
// // Global var to hold number of guesses:
var guessCount = 1;


function playTheGame() {
    let numArray = [0,1,2,3,4,5,6,7,8,9,10]; //I could have used <=10 && >=0 instead.
    let start = confirm("Start playing?");
    if (start == false) {
        alert("No problem, Goodbye");
    } else {
        userNumber = parseInt(prompt("Enter a number between 0 and 10"));
        if (isNaN(userNumber)) {
            return alert("Sorry Not a number, Goodbye");
            ////////////Todo: while loop - continue asking for a valid number:
        } else if (numArray.includes(userNumber)  === false) {
            return alert("Sorry it’s not a good number, Goodbye");
        } else {
            let computerNumber = Math.floor(Math.random() * 11); //between 0-10
            console.log(computerNumber);
            return test(userNumber,computerNumber) //returning the test function 
        }
    }
}

function test(userNumber,computerNumberRounded) {
        // console.log(computerNumber)
        console.log(computerNumberRounded)
    if (userNumber == computerNumberRounded) {
        return alert("winner!") 
    } else if (userNumber > computerNumberRounded) {
        alert("Your number is bigger then the computer’s, guess again");
        alert("This was your " + guessCount + " guessing") 
        userNumber = prompt("Try again! insert another number between 0 to 10");
        // Fail out if too many guesses have been tried
        guessCount += 1;
        if (guessCount >= 3) {
            return alert('This was your 3rd guessing - Game over')
        } else {
            return test(userNumber,computerNumberRounded)
        }
        
    } else {
        alert("Your number is smaller then the computers, guess again");
        alert("This was your " + guessCount + " guessing")
        userNumber = prompt("Try again! insert another number between 0 to 10");
        // Fail out if too many guesses have been tried
        guessCount += 1;
        if (guessCount >= 3) {
            return alert('This was your 3rd guessing - Game over')
        } else {
            return test(userNumber,computerNumberRounded)
        }
        
    } 
}

// // no need to call it, we call the function from the html button
// // playTheGame()

