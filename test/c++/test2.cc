#include <iostream>
using namespace std;

float celsiusToFahrenheit(float celsius) {
    return (celsius * 9 / 5) + 32;
}

float fahrenheitToCelsius(float fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

int main() {
    int opcion;
    float temperatura;

    cout << "Seleccione la opción:" << endl;
    cout << "1. Convertir de Celsius a Fahrenheit" << endl;
    cout << "2. Convertir de Fahrenheit a Celsius" << endl;
    cin >> opcion;

    switch (opcion) {
        case 1:
            cout << "Ingrese la temperatura en grados Celsius: ";
            cin >> temperatura;
            cout << temperatura << " grados Celsius equivalen a " << celsiusToFahrenheit(temperatura) << " grados Fahrenheit" << endl;
            break;
        case 2:
            cout << "Ingrese la temperatura en grados Fahrenheit: ";
            cin >> temperatura;
            cout << temperatura << " grados Fahrenheit equivalen a " << fahrenheitToCelsius(temperatura) << " grados Celsius" << endl;
            break;
        default:
            cout << "Opción no válida" << endl;
    }

    return 0;
}
