const dot = document.querySelector('.dot');
const sc = document.querySelector('.sc');
dot.onclick = function(){
    dot.classList.toggle('active');
    sc.classList.toggle('active');  
}



document.addEventListener("mousemove", function(e){
    const dot = document.querySelector('.dot');
    dot.style.left = e.pageX + 'px';
    dot.style.top = e.pageY + 'px';
})