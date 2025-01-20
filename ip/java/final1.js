let todo = document.getElementById("todo")
let btn = document.getElementById("btn")
let liste = document.querySelector("#liste")

btn.addEventListener('click',ekle)

function ekle(){
    let li = document.createElement("li")
    li.innerHTML = todo.value
    todo.value = ""
    liste.appendChild(li)
}