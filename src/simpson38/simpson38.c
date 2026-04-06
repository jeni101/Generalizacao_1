#include <stdio.h>
#include <math.h>

double f(double x) {
    return x * x;
}

double trapezio_generalizado(double a, double b, int n) {
    double h, soma, x;
    int i;

    h = (b - a) / n;

    soma = (f(a) + f(b)) / 2.0;

    for (i = 1; i < n; i++) {
        x = a + i * h;
        soma = soma + f(x);
    }

    return soma * h;
}

int main() {
    double a = 0.0;
    double b = 1.0;
    int n = 100;

    double resultado = trapezio_generalizado(a, b, n);

    printf("O resultado da integral e: %lf\n", resultado);

    return 0;
}