let button = document.querySelectorAll('.calc div')
let inputField = document.querySelector('input')
let equals = document.querySelector('.special')
// Add an event listener to the input field

inputField.addEventListener("keydown", function (event) {
   let allowedKeys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "/", ".", "x","Backspace"];
   let keyValue = event.key;
   console.log(keyValue)
      if(allowedKeys.includes(keyValue)){
         inputField.value = validation(keyValue)
         event.preventDefault();
      }
   else{
      event.preventDefault(); 
   }
}); 

button.forEach((div)=>{
 div.addEventListener('click',()=>{
  inputField.value = validation(getValue(div))
 })
})

function validation(char){
let inputs = inputField.value.trim(' ')
let value = inputs
if(char == 'Backspace') return inputs.slice(0,inputs.length-1);
if(inputs.length > 0 && !isNaN(inputs.slice(-1))){
   value = inputField.value + char  
}
else{
   if(!isNaN(char)) value = inputField.value + char
}
return value;
}

function getValue(element){
 let id = element.id
 let value = ''
 switch(id){
   case '*':
      value = ' x ';
      break;
   case '/':
      value = ' / ';
      break;
   case '+':
      value = ' + '
      break;
   case '-':
      value =' - '
      break;
   case '.':
      if(!dotValidation(inputField.value)) value = '.'
      break;
   case '':
      value = element.innerHTML
      if(value.length > 1) value = '';
      break; 
 }
 return value;
}

function dotValidation(str){
   let i = str.length-1;
   while(i>=0){
      if(isNaN(str[i])) break;
      i--;
   }
   return str[i] == '.';
}
equals.addEventListener('click',()=>{
 let result = inputField.value

 if(!isNaN(result.slice(-1)) && result.length>0) inputField.value = String(eval(result.replace("x","*")));
})