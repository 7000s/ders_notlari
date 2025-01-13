//console.log(document.all)
//getElementByID 

let sonuc = document.body
sonuc = document.getElementById("liste") //getElementById
sonuc = document.getElementsByTagName("li")//getElementsByTagname
sonuc = document.getElementsByClassName("item")//getElementsByClassName
sonuc = document.querySelector("li")//querySelector
sonuc = document.querySelectorAll('#liste')

// let ogr_liste = ["berat","sertaç","efe"]
// console.log(ogr_liste)
// ogr_liste.forEach(abc =>{
//     console.log(abc)
// })
// for(let i=0;i<sonuc.length;i++){
//     console.log(sonuc[i])
// }
// console.log(ogr_liste[0])

// console.log(sonuc)
function tikla(){
    console.log(sonuc)
    sonuc.childNodes[0].textContent = "Meyve İsimleri :"
    console.log(sonuc.childNodes)
    //sonuc.innerText = "<li>Karpuz</li><li>Elma</li>"
}
// sonuc.values().forEach(abc =>{
//      console.log(abc.innerText)
//      if (abc.innerText == "Muz"){
//         abc.innerText = "Portakal"
//      }
        
// })
// console.log(sonuc.childNodes)
// console.log(sonuc.children)
console.log(sonuc.firstChild)
console.log(sonuc.firstElementChild)
console.log(sonuc.lastChild)
console.log(sonuc.lastElementChild)
console.log(sonuc.previousElementSibling)//onceki kardeş element
console.log(sonuc.previousSibling)//onceki kardeş text
console.log(sonuc.nextElementSibling)//sonraki kardeş element
console.log(sonuc.nextSibling)//sonraki kardeş text
console.log(sonuc.parentElement)
console.log(sonuc.parentNode)//element ile aynı
