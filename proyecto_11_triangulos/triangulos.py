# triangulos.py

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Es un triángulo equilátero.")
    elif a == b or b == c or a == c:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("Los valores no forman un triángulo.")
