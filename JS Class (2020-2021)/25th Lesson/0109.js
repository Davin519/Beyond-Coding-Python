let box = document.querySelector('.box')
document.body.addEventListener("keydown", function(e){
    if(e.key == box.innerHTML){
        box.style.backgroundColor = "green"
    } else{
        box.style.backgroundColor = "red"
    }
})