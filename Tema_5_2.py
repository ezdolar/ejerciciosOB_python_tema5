# Escribe una función que pueda decirte si un número (número entero)
# es primo o no.

from math import sqrt, floor

def esPrimo(numero):
    if numero % 2 == 0:
        return False
    for n in range(3, floor(sqrt(numero)) + 1, 2):
        if numero % n == 0:
            return False
    return True

if __name__ == "__main__":
    print(esPrimo(245863))
