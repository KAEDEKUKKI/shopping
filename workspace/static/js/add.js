const plus =document.getElementById('plus'),
minus = document.getElementById('minus'),
num = document.getElementById('num');


function add(){
    num.value++;
}
function reduce(){
    if(num.value>1){
    num.value--;
    }
}
plus.addEventListener("click", add);
minus.addEventListener("click", reduce);