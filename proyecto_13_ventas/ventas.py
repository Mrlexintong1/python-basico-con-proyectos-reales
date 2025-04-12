# ventas.py

ventas_2022 = float(input("Ventas 2022: "))
ventas_2023 = float(input("Ventas 2023: "))

variacion = ((ventas_2023 - ventas_2022) / ventas_2022) * 100
print(f"Variación: {variacion:.1f}%")

if variacion > 20:
    print("Recomendación: Bonificación para el equipo de ventas")
elif 2 <= variacion <= 20:
    print("Recomendación: Pequeña bonificación para el equipo de ventas")
elif -10 <= variacion < 2:
    print("Recomendación: Planificación de políticas de incentivo a las ventas")
else:
    print("Recomendación: Recorte de gastos")
