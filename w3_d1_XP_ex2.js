// Exercise 2 : Users
// 1) change the name “Pete” to “Richard”.
let pete = document.body.children[1].children[1];
pete.textContent = 'Richard' 
console.log(pete);

// 2) Change each first name of the two <ul>'s to your name.
// grab both uls:
let uls = document.body.querySelectorAll('ul');
for (let ul of uls) {
    console.log(ul.firstElementChild.textContent = 'Inbar');
}
// OR 
// for the first ul:
let firstUl = document.body.children[1].children[0];
console.log("firstUl", firstUl.textContent);
// for the second ul:
let secondUl = document.body.children[2].children[0];
console.log("secondUl", secondUl.textContent);

// 3) At the end of each <ul> add a <li> that says “Hey students”.
// first creating for each ul a new li which says "hey students". and then appending the new li to the uls.
for (let ul of uls) {
    let liNew = document.createElement('li')
    liNew.innerText = 'Hey students'
    ul.append(liNew)
}

// 4) Delete the name Sarah from the second <ul>.
let removeSarah = uls[1].children[1].remove();
console.log("removeSarah", removeSarah);

// 5 - Bonus
// Add a class called student_list to both of the <ul>'s.
for (let ul of uls) {
    ul.classList.add('student_list');
}
// Add the classes university and attendance to the first <ul>.
uls[0].classList.add('university', 'attendance');


