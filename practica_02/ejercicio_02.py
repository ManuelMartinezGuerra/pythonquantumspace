lista=input('Ingrese un cadena: ')
def lista_par(lista):
    lista_par=[]
    if len(lista)<2 or len(lista)<101:
        print('Cadena no valida')
    else:
        i=1
        for i in range(len(lista)):
            if i!=0 and i%2!=0:
                car=lista[i]
                lista_par.append(car) 
    print(lista_par)            
lista_par(lista)
    


