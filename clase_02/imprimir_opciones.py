def imprimir_mensaje(opcion):
    print('Hola')
    print('Como estas')
    print(f'Elegiste la opcion {opcion}')
    print('Adios')
opcion = input('Ingresa tu opcion: ')
if opcion == '1' or opcion == '2' or opcion =='3' or opcion == '4':
    imprimir_mensaje(opcion)
else:
    print('opcion incorecta')
