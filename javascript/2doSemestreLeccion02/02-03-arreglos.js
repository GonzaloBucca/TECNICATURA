// Creacion de Array o Arreglos
// let autos = new Array("ferrari","renault", "bmw"); esta es la sintaxis vieja

const autos = ["ferrari","renault", "bmw"];
console.log(autos);

// Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i  < autos.length; i++){
    console.log(i+" : "+autos[i])
}

// Modificamos los elementos del arreglo
autos[1] = "volvo";
console.log(autos[1]);

// Agregamos nuevos valores al arreglo
autos.push("audi"); // Agregamos el elemento al final del arreglo
console.log(autos);

// Otras formas de agregar elementos al arreglo
autos[autos.length] = "porche";
console.log(autos);

// Tercera forma de agregar elementos teniendo CUIDADO
autos[6] = "renault";
console.log(autos);

// Como preguntar si es una Array o Arreglo (es lo mismo Array y Arreglo)
console.log(Array.isArray(autos)); // Devuelve un resultado booleano

console.log(autos instanceof Array);// Preguntamos si la variable es una instancia de la clase Array
