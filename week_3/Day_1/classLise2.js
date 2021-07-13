let pics = [
    "https://cdn.pixabay.com/photo/2018/10/09/18/21/kitten-3735600_1280.jpg",
    "https://cdn.pixabay.com/photo/2020/04/04/16/56/puppy-5003092_960_720.jpg",
    "https://media-cdn.tripadvisor.com/media/photo-s/17/6d/f8/0d/dauphin.jpg"
];
// ADD 3 IMAGES DYNAMICALLY ON THE PAGE
let div = document.getElementById("secondDiv");
for (let i = 0; i < pics.length;i++){
	let img = document.createElement("img");
	img.setAttribute("src", pics[i]);
	div.appendChild(img)
}

let pics = [
    "https://cdn.pixabay.com/photo/2018/10/09/18/21/kitten-3735600_1280.jpg",
    "https://cdn.pixabay.com/photo/2020/04/04/16/56/puppy-5003092_960_720.jpg",
    "https://media-cdn.tripadvisor.com/media/photo-s/17/6d/f8/0d/dauphin.jpg"
];
// ADD 1 RANDOM IMAGE ON THE PAGE
let div = document.getElementById("secondDiv");
let img = document.createElement("img");
let randomNumber = Math.floor((Math.random() * pics.length));
console.log(randomNumber)
img.setAttribute("src", pics[randomNumber]);
div.appendChild(img)