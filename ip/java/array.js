// let ogrenci_listesi = ["Halil İbo","Emrullah","Enes","M.Emin"]
// var liste = new Array("Hamza","Berat","Dogukaan")
// //ogrenci_listesi[2] = "Semih"

// ogrenci_listesi.push("Abdullah")//Listenin sonuna ekler
// ogrenci_listesi.unshift("Efe")//Listenin başına ekler
// //a = liste.pop()//Listenin sonundaki elemanı siler
// //b = liste.shift()//Listenin başındaki elemanı siler

// //console.log(a,b)
// console.log(ogrenci_listesi.length)//Listenin eleman sayısını verir.
// //console.log(ogrenci_listesi.sort())//Listeyi a-z'ye doğru sıralar
// console.log(ogrenci_listesi.reverse())//Listeyi ters çevirir.

// let yeni_liste = ogrenci_listesi.concat(liste)//İki farklı listeyi birleştirir.
// //yeni_liste.fill("ogr",3,5)//
// let str = yeni_liste.join(",")//

// console.log(ogrenci_listesi)
// console.log(liste)
// console.log(yeni_liste)
// console.log(str)
// let liste2 = str.split(",")
// console.log(liste2)
// for(let i=0;i<liste2.length;i++){
//     console.log(liste2[i])
// }
// console.log("*****************************************")
// ogrenci_listesi.forEach(function(eleman,index){
//     console.log(`${index}. index : ${eleman}`)
// })
// console.log("*****************************************")
// liste.forEach((abc,i) =>{
//     console.log(`${i}. index : ${abc}`)
// })
//Branşlar listesi hazırlanacak ilk seferde 7 branş olsun
/*
    1.Sonradan listesinin başına "BT" sonuna "İdari" bransı eklensin
    2.Listenin eleman sayısı yazdırılsın
    3.Liste alfabetik olarak sıralansın
    4.Listenin her bir elemanı ekrana yazdırılsın.
*/

let p = document.getElementsByTagName("p");
let p2 = document.getElementById("prg")
var baslik = document.querySelector("#baslik")
console.log(p)
console.log(p2)
console.log(baslik)
function degistir(){
    p[0].innerText = "BT İletişim"
    p2.innerText = "Topçu"
}