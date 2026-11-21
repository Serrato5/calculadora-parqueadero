# Calculadora de parqueadero - Sebastián Serrato
# Calcula el cobro de motos y carros por horas, con tope diario.

tarifas = {1: ("Motocicleta", 2000, 12000),
           2: ("Automóvil", 4000, 24000)}

try:
    tipo = int(input("Tipo de vehículo (1 moto, 2 carro): "))
    horas = int(input("Horas de permanencia: "))
except ValueError:
    print("Error: ingrese números enteros.")
else:
    if tipo not in tarifas:
        print("Error: tipo de vehículo inválido.")
    elif not 1 <= horas <= 24:
        print("Error: las horas deben estar entre 1 y 24.")
    else:
        vehiculo, tarifa, maximo = tarifas[tipo]
        clasificacion = ("Corta" if horas <= 2
                         else "Media" if horas <= 5
                         else "Prolongada")
        valor = horas * tarifa
        total = min(valor, maximo)
        print("Vehículo:", vehiculo)
        print("Permanencia:", clasificacion)
        print(f"Valor por horas: ${valor:,}")
        print("Tope aplicado:", "Sí" if valor > maximo else "No")
        print(f"Total a pagar: ${total:,}")
