#include <iostream>

int main() {
    // Declarar variables para almacenar los números ingresados por el usuario
    int numero1, numero2;
    
    // Pedir al usuario que ingrese el primer número
    std::cout << "Ingrese el primer número: ";
    std::cin >> numero1;
    
    // Pedir al usuario que ingrese el segundo número
    std::cout << "Ingrese el segundo número: ";
    std::cin >> numero2;
    
    // Calcular la suma de los dos números
    int suma = numero1 + numero2;
    
    // Mostrar el resultado al usuario
    std::cout << "La suma de " << numero1 << " y " << numero2 << " es: " << suma << std::endl;
    
    return 0;
}
