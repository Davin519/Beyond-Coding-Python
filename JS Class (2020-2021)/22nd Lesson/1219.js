let boxCount = 0;
let i = 0;
let startTime;
let endTime;
let arrows;
let arrow_types = {
    name:["ArrowRight", "ArrowLeft", "ArrowUp", "ArrowDown"],
    symbol:["→", "←", "↑", "↓"],
    color:["#8983ff", "#9483fd", "#94daff", "#99feff"]
}

document.querySelector(".btn").addEventListener("click", function(){
    
    boxCount = document.getElementById("ipt").value * 1;
    document.querySelector(".wrap").className = "erase_wrap";

    let ct = document.querySelector(".container");

    for(let i = 0;i<boxCount;i++){
        
        let arrow = document.createElement("div");
        let rand = Math.floor(Math.random()* 4);

        arrow.classList.add("arrow", arrow_types.name[rand]);
        arrow.innerText = arrow_types.symbol[rand];
        arrow.style.backgroundColor = arrow_types.color[rand];

        ct.appendChild(arrow);

    }

    arrows = document.querySelectorAll(".arrow");
    i = arrows.length -1;
    startTime = new Date().getTime();

})

document.body.addEventListener("keydown", function(e){

    if(arrow_types.name.includes(e.code)){
        
        if(i>-1 && arrows[i].classList.contains(e.code)){

        arrows[i].className = "disabled_arrow"
        i-=1;

            if(i == -1){
                endTime = new Date().getTime();

                setTimeout(()=>{
                    alert("Success!!" + ((endTime - startTime)/1000));
                    location.reload();
                }, 1000);
            }
        } else {
            alert("you failed...");
            location.reload();
        }
    }
})