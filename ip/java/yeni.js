// for(let i=0;i<77;i++){
//     if(i % 2 == 0){
//         console.log(i)
//     }
// }
// var i=0;
// while(i<=20){
//     if(i % 2 == 0){
//         console.log(i)
//     }
//     i++;
// }
//Ekrana 10 defa Damyo yazdırma
// var limit = parseInt(prompt("Kac defa yazdırmak istersin?"));
// for(let i=0;i<limit;i++){
//     console.log(" Damyo");
//     console.log("...");
// }
//Girilen sayının faktoriyeli bulma
//Dışarıdan girilen sayıların toplama sıfır(0) girildiğinde programı sonlandırma
// sayi = parseInt(prompt("Sayi Gir :"))
// var f = 1;
// for(let i=1;i<=sayi;i++){
//     f = f * i;
// }
// console.log("Sayinin Faktoriyeli : " + f);

// s1 = parseInt(prompt("Sayi Gir :"));
// t = 0;
// while(s1 != 0){
//     t = t + s1;
//     console.log(s1);
//     s1 = parseInt(prompt("Sayi Gir :"));
// }
// console.log("Sayıların Toplami : " + t);
sayi = parseInt(prompt("Sayi Gir :"));
flag = 1;
for(let i=2;i<=sayi/2;i++){
    if(sayi % i == 0){
        flag = 0;
        break;
    }
}
if(flag && sayi >1){
    console.log("Sayi Asal");
}else{
    console.log("Sayi Asal Değil!");
}