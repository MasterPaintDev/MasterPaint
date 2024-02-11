import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                // Pedir al usuario que ingrese el primer número
                System.out.print("Ingrese el primer número (o ingrese 'q' para salir): ");
                String input = scanner.next();

                // Verificar si el usuario quiere salir del programa
                if (input.equals("q")) {
                    System.out.println("Saliendo del programa...");
                    break;
                }

                int numero1 = Integer.parseInt(input);

                // Pedir al usuario que ingrese el segundo número
                System.out.print("Ingrese el segundo número: ");
                int numero2 = scanner.nextInt();

                // Calcular la suma de los dos números
                int suma = numero1 + numero2;

                // Mostrar el resultado al usuario
                System.out.println("La suma de " + numero1 + " y " + numero2 + " es: " + suma);
            } catch (InputMismatchException e) {
                System.out.println("Error: ¡Ingrese un número entero válido!");
                scanner.nextLine(); // Limpiar el buffer del scanner
            } catch (NumberFormatException e) {
                System.out.println("Error: ¡Ingrese un número entero válido!");
            }
        }

        // Cerrar el objeto Scanner
        scanner.close();
    }
}
