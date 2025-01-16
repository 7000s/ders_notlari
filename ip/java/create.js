let bt_liste = document.getElementById("bt-liste")
let ogr_ad = document.querySelector("#ogr-ad")

console.log(ogr_ad)
function ekle(){
    let li = document.createElement("li")
    //li.innerText = prompt("Eklemek İsdtediğninz Öğrenci İsmini Giriniz :") //<li>M.Emin</li>
    li.innerText = ogr_ad.value
    bt_liste.appendChild(li)
    console.log(ogr_ad.value)
}

function sil(){
    // bt_liste.removeChild(bt_liste.lastElementChild)
    //bt_liste.innerText = ""
    //bt_liste.removeChild(bt_liste.children[1])
    bt_liste.removeChild(bt_liste.lastChild)
}