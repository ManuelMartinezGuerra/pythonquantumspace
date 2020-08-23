n=100
cont=1
suma_par=0
suma_impar=0
par=[]
impar=[]
while cont<=n:
    if cont % 2 ==0:
        par.append(cont)
        suma_par=suma_par+cont
    else:
        impar.append(cont)
        suma_impar+=cont
    cont=cont+1
print(par)   
print(f'La suma de todos los pares es : {suma_par}')
print(impar)
print(f'La suma de todos los impares es : {suma_impar}')