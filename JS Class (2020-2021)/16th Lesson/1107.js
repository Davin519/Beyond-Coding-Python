let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');

canvas.width = window.innerWidth - 100;
canvas.height = innerHeight - 100;

let imgDino = new Image();
imgDino.src = "t-rex.png"

let dino = {
    x:10,
    y:200,
    width:50,
    height:50,
    draw(){
        ctx.fillStyle = "green";
        //ctx.fillRect(this.x, this.y,this.width, this.height);
        ctx.drawImage(imgDino, this.x, this.y, this.width, this.height);
    }
}

let imgCactus= new Image();
imgCactus.src = "cactus.png"

class Cactus {
    constructor(){
        this.x = 500;
        this.y = 200;
        this.width = 50;
        this.height = 50;
    }
    draw(){
        ctx.fillStyle = "red";
        //ctx.fillRect(this.x, this.y,this.width, this.height);
        ctx.drawImage(imgCactus, this.x, this.y,this.width, this.height);
    }
}

let cacti = [];
let timer = 0;
let jumping = false;
let jumptimer = 0;
let animation;

function animate(){
    animation = requestAnimationFrame(animate);
    timer++;
    
    ctx.clearRect(0,0,canvas.width, canvas.height);
    
    if(timer % 150 === 0){
        let cactus = new Cactus();
        cacti.push(cactus);
    }

    cacti.forEach((a, i, o)=>{
        if(a.x < 0){
            o.splice(i, 1);
        }
        
        collisionCheck(dino, a);

        a.x -= 6;
        a.draw();
    })

    if(jumping == true){
        dino.y -= 4;
        jumptimer++;
    }

    if(jumptimer > 30){
        jumping = false
    }

    if(jumping == false && dino.y < 200){
        dino.y += 4;
        if(dino.y == 200){
            jumptimer = 0;
        }
    }

    dino.draw();
}

animate()

document.addEventListener("keydown", (e)=>{
    if(e.code === "Space"){
        jumping = true
    }
})

function collisionCheck(dino, cactus){
    let xDiff = cactus.x - (dino.x + dino.width);
    let yDiff = cactus.y - (dino.y + dino.height);
    if(xDiff < 0 && yDiff < 0){
        cancelAnimationFrame(animation);
        alert('You died')
    }
}