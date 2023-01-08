let imgBox = document.querySelector('.img-box');
let imgWrap = document.querySelector('img-wrap');
let carImg = document.getElementById('carimg');
let line = document.getElementById('line');

carImg.style.width = imgBox.offsetWidth + "px";
line.style.left = imgBox.offsetWidth = "px";

let leftSpace = imgBox.offsetLeft;

imgBox.onmousemove = function(e){
    let boxWidth = (e.pageX - leftSpace) + "px";
    imgWrap.style.width = boxWidth;
    line.style.left = boxWidth;
}
