import java.util.Scanner;

public class ConversorTemperatura {
    public static float celsiusToFahrenheit(float celsius) {
        return (celsius * 9 / 5) + 32;
    }

    public static float fahrenheitToCelsius(float fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public static float celsiusToKelvin(float celsius) {
        return celsius + 273.15f;
    }

    public static float kelvinToCelsius(float kelvin) {
        return kelvin - 273.15f;
    }

    public static float fahrenheitToKelvin(float fahrenheit) {
        return celsiusToKelvin(fahrenheitToCelsius(fahrenheit));
    }

    public static float kelvinToFahrenheit(float kelvin) {
        return celsiusToFahrenheit(kelvinToCelsius(kelvin));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        boolean continuar = true;

        while (continuar) {
            System.out.println("Seleccione la conversión:");
            System.out.println("1. Celsius a Fahrenheit");
            System.out.println("2. Fahrenheit a Celsius");
            System.out.println("3. Celsius a Kelvin");
            System.out.println("4. Kelvin a Celsius");
            System.out.println("5. Fahrenheit a Kelvin");
            System.out.println("6. Kelvin a Fahrenheit");
            System.out.println("7. Salir");
            int opcion = scanner.nextInt();

            float temperatura;
            float resultado;

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la temperatura en grados Celsius: ");
                    temperatura = scanner.nextFloat();
                    resultado = celsiusToFahrenheit(temperatura);
                    System.out.printf("%.2f grados Celsius equivalen a %.2f grados Fahrenheit\n", temperatura, resultado);
                    break;
                case 2:
                    System.out.print("Ingrese la temperatura en grados Fahrenheit: ");
                    temperatura = scanner.nextFloat();
                    resultado = fahrenheitToCelsius(temperatura);
                    System.out.printf("%.2f grados Fahrenheit equivalen a %.2f grados Celsius\n", temperatura, resultado);
                    break;
                case 3:
                    System.out.print("Ingrese la temperatura en grados Celsius: ");
                    temperatura = scanner.nextFloat();
                    resultado = celsiusToKelvin(temperatura);
                    System.out.printf("%.2f grados Celsius equivalen a %.2f grados Kelvin\n", temperatura, resultado);
                    break;
                case 4:
                    System.out.print("Ingrese la temperatura en grados Kelvin: ");
                    temperatura = scanner.nextFloat();
                    resultado = kelvinToCelsius(temperatura);
                    System.out.printf("%.2f grados Kelvin equivalen a %.2f grados Celsius\n", temperatura, resultado);
                    break;
                case 5:
                    System.out.print("Ingrese la temperatura en grados Fahrenheit: ");
                    temperatura = scanner.nextFloat();
                    resultado = fahrenheitToKelvin(temperatura);
                    System.out.printf("%.2f grados Fahrenheit equivalen a %.2f grados Kelvin\n", temperatura, resultado);
                    break;
                case 6:
                    System.out.print("Ingrese la temperatura en grados Kelvin: ");
                    temperatura = scanner.nextFloat();
                    resultado = kelvinToFahrenheit(temperatura);
                    System.out.printf("%.2f grados Kelvin equivalen a %.2f grados Fahrenheit\n", temperatura, resultado);
                    break;
                case 7:
                    continuar = false;
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción no válida");
            }
        }

        scanner.close();
    }
}
