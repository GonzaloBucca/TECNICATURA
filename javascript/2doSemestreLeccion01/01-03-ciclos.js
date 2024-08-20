//Ciclo while
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("fin del siglo while");

//Ciclo do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("fin del siglo do while");

//Ciclo for
for( let contando = 0; contando < 3; contando++){
    console.log(contando)
}
console.log("fin del siglo for");

//Palabra reservada BREAK
for(let contando = 0; contando <= 10; contando++ ){
    if(contando % 2 == 0){
        console.log(contando);  //Muestra todos los pares
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer numero par")

//La palabra CONTINUE 
for(let contando = 0; contando <= 10; contando++ ){
    if(contando % 2 !== 0){
        continue; //Ir a la siguiente iteracion
    }
    console.log(contando);
}
console.log("Termina el ciclo")

//Etiquetas labels (no son recomendables)
inicio: 
for(let contando = 0; contando <= 10; contando++ ){
    if(contando % 2 !== 0){
        break inicio; //Ir a la siguiente iteracion
    }
    console.log(contando);
}
console.log("Termina el ciclo")


