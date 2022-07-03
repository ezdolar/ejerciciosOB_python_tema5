# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no

def esBisiesto(year):
    if year % 4 == 0:
        return True
    return False

if __name__ =="__main__":
    print(esBisiesto(2020))