let lamba = document.querySelector("img")
var baslik = document.getElementById("baslik")
console.log(lamba)
console.log(baslik)
function ac(){
    lamba.setAttribute("src","../img/acik.png")
    //baslik.setAttribute("class","baslik3")
    console.log(baslik.classList)
    baslik.classList.add("baslik3")
}
function kapa(){
    lamba.setAttribute("src","../img/kapali.png")
}