// function  mesaj(){
//     console.log("Hello Emrullah");
// }
// function mesaj2(isim){
//     console.log(`Hello ${isim}`);
//     //console.log("Hello" + isim)
// }
// mesaj();
// mesaj2("Berat");
// let ad = "Sertaç";
// mesaj2(ad);
// function toplam(a,b){
//     return a+b;
// }
// console.log(toplam(3,5));
// let sonuc = toplam(7,12);
// console.log(sonuc)



// not1 = Number(prompt("Not Gir :"));
// function derskont(n1){
//     if(n1>=50) console.log("Geçti");
//     else console.log("Kaldı");
// }
// derskont(not1)

// let ogr_notlar = [56,46,20,78,98,54,25,65,30,61,41,99];
// for(let i=0;i<ogr_notlar.length;i++){
//     derskont(ogr_notlar[i])
// }


// function yazi(){
//     console.log("BT-Bilişim");   
// }
// for(i=1;i<11;i++){
//     yazi();
// }

function yazi(isim){
    console.log(`Brans adı = ${isim}`);   
}
for(i=1;i<11;i++){
    yazi("BT-Bilişim");
}
function davetiye(k){
    console.log(`Sayın ${k} Mezuniyetime davetlisiniz`);
}

davetli_listesi = ["Emirhan","Semih","Harun"];
for(i=0;i<davetli_listesi.length;i++){
    davetiye(davetli_listesi[i])
}
    