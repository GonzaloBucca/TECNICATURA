//Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se repetira hasta que se introduzca un 0
// Hacer este ejercicio con la clase Scanner, luego hacerlo nuevamente con la clase JOptionPane
package Ciclos02;

import javax.swing.JOptionPane;


public class Ciclos02 {
    public static void main(String[] args) {
       
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro nuemro"));
        }
        JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
    }
}

