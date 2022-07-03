#Escribe una función que calcule el área de un triángulo,
#recibiendo la altura y la base como parámetros y otra función que
# calcule el área de un círculo recibiendo el radio del mismo

from math import pow, pi

def calcAreaTriangulo(base, altura):
    return (base * altura) / 2

def calcAreaCirculo(radio):
    return pi * radio ** 2

if __name__ == "__main__":
    print("%.2f cm2" % calcAreaTriangulo(2, 4))
    print("%.2f cm2" % calcAreaCirculo(5))