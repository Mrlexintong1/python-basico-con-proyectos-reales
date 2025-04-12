# combustible.py

tipo = input("Tipo de combustible (E/D): ").upper()
litros = float(input("Litros vendidos: "))

if tipo == 'E':
    precio_litro = 1.70
    descuento = 0.02 if litros <= 15 else 0.04
elif tipo == 'D':
    precio_litro = 2.00
    descuento = 0.03 if litros <= 15 else 0.05
else:
    print("Tipo inválido")
    exit()

total_sin_descuento = precio_litro * litros
descuento_total = total_sin_descuento * descuento
total_final = total_sin_descuento - descuento_total

print(f"Total a pagar con descuento: R$ {total_final:.2f}")
