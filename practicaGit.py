def suma(x,y):
    return x+y
print(suma(2,4))

def multiplicacion(x,y):
    return x*y
print(multiplicacion(2,4))

def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("No se puede dividir un número entre 0")
print(division(4,0))