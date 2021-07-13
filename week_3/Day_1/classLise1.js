//PROPERTIES
let divfromHTML = document.body.children[0];
console.log(divfromHTML)
let h1fromHTML = divfromHTML.firstElementChild;
console.log(h1fromHTML)
let textfromH1 = h1fromHTML.textContent;
console.log(textfromH1);
h1fromHTML.textContent = "Hello Students";
h1fromHTML.style.backgroundColor = "yellow";
//METHODS
let title = document.getElementById("firstTitle");
console.log(title)
let tests = document.getElementsByClassName("test");
console.log(tests)
let paragraph = document.getElementsByTagName("p")[0];
console.log(paragraph)
let allTests = document.querySelectorAll("h1,p");
console.log(allTests)
// APPEND ELEMENTS
//create the element
let h2 = document.createElement("h2");
// //add text to the element
// h2.textContent = "New H2 added on the page";
let text = document.createTextNode("Added new H2");
h2.appendChild(text);
//retrieve the element where I want to add the h2
let div = document.getElementById("secondDiv");
//add the element AT THE END OF THE DIV
div.appendChild(h2)