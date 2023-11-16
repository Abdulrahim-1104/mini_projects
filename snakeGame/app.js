let canva = document.getElementById('canva');
let context = canva.getContext("2d");
let score = document.getElementById('scoreval')
let info = document.getElementById('info')
let scoreVal = 0
const UNIT = 25;
let xVel = UNIT;
let yVel = 0;
let foodX;
let foodY;
let bool = false;
const WIDTH = HEIGHT = 500;
let snakeBody = [
 {x:2*UNIT,y:0},
 {x:1*UNIT,y:0},
 {x:0*UNIT,y:0}
]
window.addEventListener('keydown',keyPress)
startGame();

function startGame(){
board()
food()
foodDisplay()
snakeFill()
}

setInterval(()=>{
 if(bool){
 board()
 foodDisplay()
 snakeFill()
 collision()
 snakeMove()
 info.innerHTML = ''
 }
 },100)

function board(){
 context.fillStyle = 'black'
 context.fillRect(0,0,WIDTH,HEIGHT)
}
function food(){
 foodX = Math.floor(Math.random()*20)*UNIT
 foodY = Math.floor(Math.random()*20)*UNIT
}
function snakeFill(){
 context.fillStyle = 'aliceblue'
 context.strokeStyle = 'black'
 snakeBody.forEach((s)=>{
 context.fillRect(s.x,s.y,UNIT,UNIT)
 context.strokeRect(s.x,s.y,UNIT,UNIT)
})
}
function snakeMove(){
let obj = {x:snakeBody[0].x+xVel,y:snakeBody[0].y+yVel}
if(snakeBody[0].x == foodX && snakeBody[0].y == foodY){
 snakeBody.unshift(obj)
 scoreVal += 1
 score.innerHTML = scoreVal 
 food()
}
snakeBody.unshift(obj)
snakeBody.pop()
}
function foodDisplay(){
 context.fillStyle = 'blue'
 context.fillRect(foodX,foodY,UNIT,UNIT)
}
function collision(){
 let x =  snakeBody[0].x
 let y = snakeBody[0].y
 if (x==WIDTH || y==HEIGHT || x==-UNIT|| y==-UNIT){
  gameOver()
  bool=false;
 }
 for(let i=2;i<snakeBody.length;i++){
  if(snakeBody[i].x == x && snakeBody[i].y == y){
   gameOver()
   bool = false
  }
 }
}
function gameOver(){
 board()
 context.font = '40px Arial';
 context.fillStyle = 'blue';  
 const text1 = 'GAME OVER';
 const text2 = 'Press any key to start again'
 const x = 120; 
 const y = 100; 
 context.fillText(text1, x, y);
}
function keyPress(event){
 bool = true
 const LEFT = 37 
 const UP = 38
 const RIGHT = 39
 const DOWN = 40
 switch(event.keyCode){
  case LEFT:
   if(xVel != UNIT){
    xVel = -UNIT
    yVel = 0
   }
   break
  case UP:
   if(yVel != UNIT){
    xVel = 0
    yVel = -UNIT
   }
   break
  case RIGHT:
   if(xVel != -UNIT){
   xVel = UNIT
   yVel = 0
   }
   break
  case DOWN:
   if(yVel != -UNIT){
   xVel = 0
   yVel = UNIT
   }
   break
 }
}
