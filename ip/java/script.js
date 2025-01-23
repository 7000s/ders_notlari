/*
function fonksiyon_adi(param1,param2,....){
    komut1;
    komut2;
    ....
    komut n;
}
*/
function mesajyaz(){
    console.log("Hello Emrullah");
}
function mesajyaz2(isim){
    console.log(`Hello ${isim}`);
    //console.log("Hello " + isim)
}
mesajyaz();
mesajyaz2("Berat");
let ad= "Sertaç";
mesajyaz2(ad);
function toplama(a,b){
    return a+b;
}
console.log(toplama(3,5));
let sonuc = toplama(7,12);
console.log(sonuc)
//Dışarıdan girilen not değeri için Geçti veya Kaldı sonucunu veren fonksiyon
not1 = parseInt(prompt("Not Gir :"));
//console.log(not1)
function dersKontrol(n1){
    if(n1>=50) console.log("Geçti");
    else console.log("Kaldi");
}
let ogrenci_notlari = [75,68,40,32,85,94,25,77,35,96,81,48,60,74];
for(let i=0;i<ogrenci_notlari.length;i++){
    dersKontrol(ogrenci_notlari[i])
}
dersKontrol(not1);