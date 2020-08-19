n1 = float(input('Por favor introduzca el primer número : '))
n2 = float(input('Por favor introduzca el segundo número : '))
n3 = float(input('Por favor introduzca el tercer número : '))
if n1 > n2 > n3 :
    print(f'El mayor es : {n1}')
    print(f'El menor es: {n3}')
elif n1 == n2 :
    print('Error no puede introducir digitos iguales')
elif n2 == n3 :
    print('Error no puede introducir digitos iguales')
elif n1 == n3 :
    print('Error no puede introducir digitos iguales')