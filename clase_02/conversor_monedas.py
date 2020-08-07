mensaje = """
Hola señor, este es un convensor de monedas
Ingresa cualquier de estas 3 opciones:
1 = soles - dolares
2 = pesos colombianos - dolares
3 = euros - dolares
"""
print(mensaje)
opcion = int(input('ingrese la opcion: '))
if opcion == 1:
    tipo_de_cambio = 0.28
    monto = float(input('Hola, ingresa tu monto en soles: '))
    monto_dolares = round(monto * tipo_de_cambio, 2)
    print(f'El monto en dolores es: {monto_dolares}')
elif opcion == 2:
    tipo_de_cambio = 1.19
    monto = float(input('Hola ingresa tu monto en euros: '))
    monto_dolares= round(monto * tipo_de_cambio, 2)
    print(f'El monto en dolares es : {monto_dolares}')
elif opcion == 3:
    tipo_de_cambio = 0.00027
    monto = float(input('Hola, ingrese su monto en pesos'))
    monto_dolares = round(monto * tipo_de_cambio, 2)
    print(f'El monto en dolares es: {monto_dolares}')

