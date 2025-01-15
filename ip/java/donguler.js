// for(let i=0;i<77;i++){
//     if(i % 2 == 0){
//         console.log(i)
//     }
// }
// var i = 0;
// while(i<=20){
//     if(i % 2 == 0){
//         console.log(i)
//     }
//     i++;
// }

// for(let i=0;i<=10;i++){
//         console.log(i + " damyo")
// }

// let sayi = Number(prompt("sayi gir :"))
// for(let i=1;i<=sayi;i++){
//     console.log(i + " damyo")
// }

// sayi = Number(prompt("sayi gir :"))
// var f = 1;
// for(let i=1;i<=sayi;i++){
//     f  = f*i;
// }
// console.log("sayinin faktöriyeli : " + f)

// s1 = Number(prompt("sayi gir :")) //sayilarin toplamı
// t = 0
// while(s1 != 0){
//     t = t + s1;
//     console.log(s1)
//     s1 = Number(prompt("sayi gir :"));
// }
// console.log("sayilarin toplamı : " + t);

sayi = Number(prompt("sayi gir :"))
for(let i=2;i<sayi/2;i++){
    if(sayi % i == 0){
        console.log(i + " değeri için tam bölünür")
    }
    else{
        console.log(i + " bölünmez")
    }
}