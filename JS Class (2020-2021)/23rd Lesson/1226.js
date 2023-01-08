let a = 10 //variable
const c = 30 //constant
// no need to add let var or const when rewriting variable
// you may not change const (constant)
a = 1
let b = 2
// but need to add let var or const when new variable
let d = 40
// you can use operations just like python
a + c
a - c
a * c
a / c
a % c 
// if you use % you will get remainder like 5 / 3 this shows 2

a = 237498732894
b = 384908539044

console.log(a % b)

// there are if, else if, and else (the three conditions)
if (a > 5){
    console.log("a is larger than 5")
}
else if (a < 5){
    console.log("a is smaller than 5")
}
else {
    console.log("a is equal 5")
}
// for(let i = 0;i<10;i++){
//     console.log(i)
// }

// for(let i = 100; i < 103; i++){
//     console.log(i)
//     for (let j = 0; j < 3; j++){
//         console.log(j)
//     }
// }
for(let j = 1; j < 10; j++){
    for(let i = 1; i < 10;i++)
    console.log(i + "*" + j + "=" + (i*j))
}
