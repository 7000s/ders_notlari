/* 
var:
-yeniden tanımlamaya izim verir
- scop ({}) içine erişir yani scope içinde olsa bile erişir ve o değeri yazar

let:
-aynı alanda bir kez tanımlanabilir

const:
-bir kez tanımlanabilir, değişikliğe izin vermez



*/
//var a = 10;
// {
//     //var a = 25;
//     let a = 41;
//     console.log(a)
// }
// const a = 58;
// console.log(a)

//  b = 4;
//  b++; // 1 arttır
//  console.log(b)//5
//  console.log(b++)//5 önce kullan sonra arttır
//  // şuan b = 6
//  console.log(++b)//7 önce arttır sonra kullan
//  console.log(b)//7
//  let c = ++b;
//  console.log(c)

let tabur_kontrol = 1;
if(tabur_kontrol = 0){
    console.log("ogrenci no al")
}
let sayi = Number(prompt("sayi gir :"))
if(sayi % 2 == 0){
    console.log("çift")
}
else{
    console.log("tek")
}

sıcaklık_degeri = Number(prompt("sıcaklık değeri gir :"))
if(sıcaklık_degeri<0){
    console.log("kıs mevsimi")
}
else if(sıcaklık_degeri>15){
    console.log("yaz mevsimi")
}
else{
    console.log("ilkbahar ya da sonbahar")
}