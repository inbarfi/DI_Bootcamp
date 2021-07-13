// xpExercise1 
// Move the red box from left to right

// getting the red box
let animateBox = document.getElementById('animate');
// getting the yellow box
let containerBox = document.getElementById('container');
let id;
let left=0;
// getting container width so animateBox stops before its max width
let containerBoxWidth = containerBox.offsetWidth;
console.log(containerBoxWidth);


function move() {
    id = setInterval(function(){
        if (left > containerBoxWidth - 60) {
            stop(); 
            // return; //no need for return if we put the else. set return so it won't go to the else part - it takes time to stop it and in this time it goes to the else part.
        } 
        else { left += 5;
        // box.style.left = left + 'px';
        animateBox.style.left = `${left}px` }
    }, 5)
}

function stop() {
  clearInterval(id)
}

// Exercise 2: Drag & Drop
// 1. Create a draggable square/box element in your HTML file. //box1 & box2
// 2. add the functionality which will allow you
//    to drag the square/box and drop it into the larger box.

// getting box1, box2
let box1 = document.getElementById('box1');
let box2 = document.getElementById('box2');
console.log(box1);
// set attribute dragable
box1.setAttribute('draggable', 'true'); //gg
// adding eventListener to box1 for event 'dragable'
box1.addEventListener('dragstart', dragstart_fun);
// adding eventListener to box2 for event 'drop'
box2.addEventListener('drop', drop_fun);
box2.addEventListener('dragover', dragover_fun)
function dragover_fun(e){
    e.preventDefault(); //important because the default is to reject elements. read more about it 
    console.log('dragover');
    e.dataTransfer.dropEffect = 'link'; //important! 
}

// creating the dragstart_fun
function dragstart_fun(e){
    console.log('start', e.target.id);
    e.dataTransfer.setData('text/plain',e.target.id);
} 
// creating the drop_fun
function drop_fun(e){
    console.log('somethign');
    e.preventDefault();
    const data = e.dataTransfer.getData('text/plain'); //for files: const data = e.dataTransfer.files;
    console.log(data);
    e.target.appendChild(document.getElementById(data)) //in this case data contains the id
}