# operaciones.py

def analizar_resultado(resultado):
    print(f"Resultado: {resultado}")
    print("Es un número positivo" if resultado > 0 else "Es un número negativo" if resultado < 0 else "Es cero")
    print("Es un número entero" if resultado == int(resultado) else "Es un número decimal")
    if resultado == int(resultado):
        print("Es un número par" if int(resultado) % 2 == 0 else "Es un número impar")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Seleccione la operación (+, -, *, /): ")

if operacion == '+':
    res = num1 + num2
elif operacion == '-':
    res = num1 - num2
elif operacion == '*':
    res = num1 * num2
elif operacion == '/':
    res = num1 / num2 if num2 != 0 else 0
else:
    print("Operación inválida")
    exit()

analizar_resultado(res)
