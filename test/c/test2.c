#include <stdio.h>

float celsiusToFahrenheit(float celsius) {
    return (celsius * 9 / 5) + 32;
}

float fahrenheitToCelsius(float fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

int main() {
    int opcion;
    float temperatura;

    printf("Seleccione la opción:\n");
    printf("1. Convertir de Celsius a Fahrenheit\n");
    printf("2. Convertir de Fahrenheit a Celsius\n");
    scanf("%d", &opcion);

    switch (opcion) {
        case 1:
            printf("Ingrese la temperatura en grados Celsius: ");
            scanf("%f", &temperatura);
            printf("%.2f grados Celsius equivalen a %.2f grados Fahrenheit\n", temperatura, celsiusToFahrenheit(temperatura));
            break;
        case 2:
            printf("Ingrese la temperatura en grados Fahrenheit: ");
            scanf("%f", &temperatura);
            printf("%.2f grados Fahrenheit equivalen a %.2f grados Celsius\n", temperatura, fahrenheitToCelsius(temperatura));
            break;
        default:
            printf("Opción no válida\n");
    }

    return 0;
}
