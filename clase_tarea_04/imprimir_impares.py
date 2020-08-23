def numeros_impares() :
    contador = 0
    for n in range(101):
         if n%2 != 0:
             contador += 1
             print(n)
    print(f'La cantidad de impares es : {contador}')
numeros_impares()

        
