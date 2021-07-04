// Ex_1

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
//1. Remove Banana from the array:
console.log(fruits.shift())
console.log(fruits)
//2. Sort the array in alphabetical order:
console.log(fruits.sort())
//3. Add “Kiwi” to the end of the array:
console.log(fruits.push("Kiwi"))
console.log(fruits)
//4.Remove “Apples” from the array. Don’t use the same method as in part 1:
console.log(fruits.splice(0,1))
console.log(fruits)
//5. Sort the array in reverse order. (Not alphabetical):
console.log(fruits.reverse())

// Ex_2
// 1.Access and then console.log “Oranges”:
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(fruits[1, 1])

