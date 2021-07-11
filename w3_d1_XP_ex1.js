// Exercise 1 : 

// 1) Change The Navbar
// In the <div>, change the value of the id attribute from 
// navBar to socialNetworkNavigation, using the setAttribute method.
// element.setAttribute(attribute, value):
let navBar = document.body.children[0]; 
console.log(navBar);
navBar.setAttribute('id', 'socialNetworkNavigation');
console.log(navBar);

// 2) 1. create a new <li> tag (use the createElement method document.createElement(element))
let liNew = document.createElement('li');
//    2. Create a new text node with “Logout” as its specified text
let text = document.createTextNode('Logout');
//    3. Append the text node to the newly created list node (li)
liNew.appendChild(text);
//    4. Finally, append this updated list node to the unordered list above, using the appendChild method
let ul = navBar.querySelector('ul')
ul.appendChild(liNew);

// 3) Bonus - Use the firstElementChild and the lastElementChild properties to retrieve
//  the first and last li elements from their parent element (ul). Display the text of each link.
// (Hint: use the textContent property).

let firstChild = ul.firstElementChild
let lastChild = ul.lastElementChild
console.log("first child: ", firstChild.textContent)
console.log("last child: ", lastChild.textContent)
