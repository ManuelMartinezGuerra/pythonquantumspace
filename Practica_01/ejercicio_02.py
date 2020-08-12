n1 = float(input('Ingrese la altura de un poligono: '))
n2 = float(input('Ingrese la base de un poligono: '))
if n1 == n2 :
    area = round(n1 * n2)
    print(f'El area del cuadrado es: {area}')
elif n1 != n2 :
    perimetro = n1 + n2 + n1 + n2
    print(f'El perimetro del rectangulo es : {perimetro}')

