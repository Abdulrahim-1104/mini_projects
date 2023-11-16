let cards = [
 {name:'hippo',itag:'<i class="fa-solid fa-hippo"></i>'},
 {name:'hippo',itag:'<i class="fa-solid fa-hippo"></i>'},
 {name:'otter',itag:'<i class="fa-solid fa-otter"></i>'},
 {name:'otter',itag:'<i class="fa-solid fa-otter"></i>'},
 {name:'dragon',itag:'<i class="fa-solid fa-dragon"></i>'},
 {name:'dragon',itag:'<i class="fa-solid fa-dragon"></i>'},
 {name:'spider',itag:'<i class="fa-solid fa-spider"></i>'},
 {name:'spider',itag:'<i class="fa-solid fa-spider"></i>'},
 {name:'dog',itag:'<i class="fa-solid fa-dog"></i>'},
 {name:'dog',itag:'<i class="fa-solid fa-dog"></i>'},
 {name:'cat',itag:'<i class="fa-solid fa-cat"></i>'},
 {name:'cat',itag:'<i class="fa-solid fa-cat"></i>'},
]

let count = 0;
let bool = true;
let flippedCard = [];
let gameboard = document.querySelector('.gameboard')
const timeOut = 500
const displayWon = 'YOU WON THE GAME'

startgame(); // game start from here

function startgame(){ // first this shuffle the cards and add classes
 for(let i=cards.length-1;i>=0;i--){
     let rand = Math.floor(Math.random()*(i+1));
     [cards[i],cards[rand]] = [cards[rand],cards[i]]
     let div = document.createElement('div')
     div.id = i 
     div.classList.add('backside')
     gameboard.appendChild(div)
     div.addEventListener('click',()=>{
      if(bool) play(div,i)
    })
}
}
function play(element,ind){ // this trak flipping
     element.classList.remove('backside')
     element.classList.add('flip')
     element.innerHTML = cards[ind].itag
     if(flippedCard.length == 0 || flippedCard[0].id != element.id){
       flippedCard.push({n:cards[ind].name,e:element,id:ind})  
     }
     if(flippedCard.length==2) {
      bool = false
      setTimeout(checkCards,timeOut)
     }
}
function checkCards(){ // this will check matching cards
 let card1 = flippedCard[0]
 let card2 = flippedCard[1]
 if(card1.n == card2.n && card1.id != card2.id){ 
       card1.e.style.visibility = 'hidden';
       card2.e.style.visibility= 'hidden';
       count +=1 
 }
 else{
       card1.e.classList.remove('flip')
       card2.e.classList.remove('flip')
       card1.e.classList.add('backside')
       card2.e.classList.add('backside')
       card1.e.innerHTML =''
       card2.e.innerHTML =''
 }
 if(count==cards.length/2){
      gameboard.remove()
      let won = document.getElementById('won')
      won.innerHTML = displayWon
 }
 flippedCard = [];
 bool = true;
}
