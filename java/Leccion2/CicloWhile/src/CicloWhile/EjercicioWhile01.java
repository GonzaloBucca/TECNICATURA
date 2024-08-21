//Si la condicion es verdadera va a ejecutarse en bucle hasta que la condicion sea falsa y ahi termina la repeticion del ciclo
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }
        
       // Ciclo DoWhile
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
           }while (contador < 7 );
        
        // Ciclo For
        for(var contando = 0; contando < 7; contando++ ){
            System.out.println("contando = " + contando); 
        } 
        // Ciclo For con BREAK
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 == 0){
               System.out.println("contando = " + contando);  
              break;
    }
 
}
        // Palabra CONTINUE
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 != 0){
            continue; // Vamos a la siguiente iteracion
               }
            System.out.println("contando = " + contando);  
              
}
        // Etiquetas LABELS
        inicio:
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 == 0){
            
                break inicio; 
               }
             }
        
        inicio:
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 != 0){
            continue inicio; // Vamos a la siguiente iteracion
               }
            System.out.println("contando = " + contando); 
        
}
}
}