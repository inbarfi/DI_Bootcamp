// // class_exercise_1:
// // 1)
// let a = document.body.children[0];
// let b = document.body.firstElementChild;
// //  2)
// let c = document.body.children[1];
// let d = document.body.children[0].nextElementSibling;
// // 3)
// let e = document.body.children[1].lastElementChild;
// let f = document.body.children[1].children[1];
// console.log("f", f);

// // class_exercise_2:
// // 1) the div:
// let a = document.getElementById('container');
// let b = document.body.querySelector('#container');

//  2)  The ul nodes, and render all of theirs children one by one (all ul):
let c = document.querySelectorAll('ul.list'); // why doesn't it work without ul. ?
// for (let ul of c) {
//     for (let li of ul.children) {
//         console.log(li.textContent);
//     }
// }

let d = document.getElementsByClassName('list');
// for (let ul of d) {
//     for (let li of ul.children) {
//         console.log(li.textContent);
//     }
// }

//  3) The first li of each ul:
for (let ul of d) {
    console.log(ul.firstElementChild);
}
// OR:
let firstUlFirstLi = c[0].children[0];
// console.log(firstUlFirstLi);
let secondUlFirstLi = c[1].children[0];
// console.log(secondUlFirstLi);
let sameFirstUlFirstLi = document.querySelector('ul.list li') //only first ul as querySelector() returns the first Element within the document that matches the specified selector
let sameSecondUlFirstLi = c[1].querySelector('li')
console.log(firstUlFirstLi === sameFirstUlFirstLi); //true
console.log(secondUlFirstLi === sameSecondUlFirstLi); //true
