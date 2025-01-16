let btn1 = document.getElementById("btn1")
let btn2 = document.getElementById("btn2")
let btn3 = document.getElementById("btn3")
let btn4 = document.getElementById("btn4")
let btn5 = document.getElementById("btn5")
let btn6 = document.getElementById("btn6")
let btn7 = document.getElementById("btn7")
let btn8 = document.getElementById("btn8")
let btn9 = document.getElementById("btn9")
let btn10 = document.getElementById("btn10")


let box = document.querySelector('.box')

btn1.addEventListener('click',function(){
    console.log("Btn1 Tiklandi...")
    box.style.backgroundColor = "#4a5e22"
})

btn2.addEventListener('click',renkDegistir)
btn3.addEventListener('click',renkDegistir)

function renkDegistir(){
    box.style.backgroundColor = "#d3aee8"
    console.log("test")
}
btn4.addEventListener('mousemove',renkDegistir)
btn5.addEventListener('mouseover',renkDegistir)
btn6.addEventListener('mouseleave',renkDegistir)
btn7.addEventListener('mouseout',renkDegistir)
btn8.addEventListener('mouseup',renkDegistir)
btn9.addEventListener('mousedown',renkDegistir)
btn10.addEventListener('mouseenter',renkDegistir)