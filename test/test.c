#include <stdio.h>

int main() {
    // Declarar variables para almacenar los números ingresados por el usuario
    int numero1, numero2;
    
    // Pedir al usuario que ingrese el primer número
    printf("Ingrese el primer número: ");
    scanf("%d", &numero1);
    
    // Pedir al usuario que ingrese el segundo número
    printf("Ingrese el segundo número: ");
    scanf("%d", &numero2);
    
    // Calcular la suma de los dos números
    int suma = numero1 + numero2;
    
    // Mostrar el resultado al usuario
    printf("La suma de %d y %d es: %d\n", numero1, numero2, suma);
    
    return 0;
}
