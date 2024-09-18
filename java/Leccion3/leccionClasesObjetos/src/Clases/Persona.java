// Una clase es una PLANTILLA
// Un objeto es una instancia de una clase
package Clases;

public class Persona {
   //Atributos de la clase (Caracteristicas)
    String nombre;
    String apellido;
    
    // Metodos de las clases (Acciones)
    public void obtenerInformacion(){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
    }
}
