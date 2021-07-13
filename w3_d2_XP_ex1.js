// xp_ex1

// 1) Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
let lastP = document.body.children[0].children[6];
lastP.parentElement.removeChild(lastP);
// or: 
// document.body.children[0].children[6].remove; //why this doesnt work like the below code?
// document.querySelector('p:last-child').remove()


// 2) Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
let h2New = document.body.children[0].children[1];
console.log(h2New);
h2New.addEventListener('click', changeBackgrColor);

function changeBackgrColor(event){
    h2New.style.backgroundColor = "red";
}

// OR:
// document.querySelector('h2').addEventListener('click', (e) => { //? what's =>
//     e.target.style.backgroundColor = "red";
// })

// 3) Set the font size of the h1 tag to a random pixel size between 0 to 100.
// document.querySelector('h1').style.fontSize = randomNumber(0, 100) + 'px' //? random number is not defined

// 4) Add an event listener which will hide the h3 when it’s clicked on (use the display property).
h3New = document.querySelector('h3');
h3New.addEventListener('click', hide);
function hide(event) {
    event.target.style.display = 'none';
}

// 5) Add a <button> when clicked on make the text of all paragraphs, bold.
let button = document.createElement("button");
button.innerHTML = "Change font";
document.body.appendChild(button);
button.addEventListener("click", Bold);
function Bold() {
    document.body.style.fontWeight = "bold";
}

// 6) When the “Submit” button of the form is clicked:
// - get the values of the input tags
// - make sure that they are not empty, //if
// - then append them to a HTML table, in the div, below the form. //else

// getting submit:
let submit = document.getElementById("submit");
submit.addEventListener("click", getValues);

function getValues(event) {
let form = document.getElementsByTagName("form")[0];
console.log(form);
let valueFname = form.elements.fname.value;
    console.log(valueFname)
    let valueLname = form.elements.lname.value;
    console.log(valueLname)
    if(valueFname.length < 2 || valueLname < 2){
        alert("please fill in at least 2 characters");
    } else {
        let div = document.getElementsByTagName("div")[0];
        let table = document.createElement("table");
        let row = table.insertRow(0)
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = valueFname
        cell2.innerHTML = valueLname
        div.appendChild(table)
    }
    event.preventDefault()
}

//  7) When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google).
// getting the second p:
let secondP = document.body.children[0].children[4];
console.log(secondP);
secondP.addEventListener("mouseover", function () {
    secondP.style.opacity = "0.2"
    secondP.style.transition = "0.5s"
});
