// Exercise 3 : Users And Style

//  1) Add a “light blue” background color and some padding to the <div>.
let div = document.body.children[0];
div.style.backgroundColor = 'lightblue';

//  2) Do not display the first name (John) in the list.
let john = document.body.children[1].children[0];
console.log(john);
john.style.display = 'none';

// 3) Add a border to the second name (Pete).
let pete = document.body.children[1].children[1];
pete.style.border = '1px solid red';

// 4) Change the font size of the whole body.
document.body.style.fontSize = '40px';

// 5) Bonus: If the background color of the div is “light blue”, 
//    alert “Hello x and y” (x and y are the users in the div).
if (div.style.backgroundColor === 'lightblue') {
    alert(`Hello ${john.textContent} and ${pete.textContent}`);
}

