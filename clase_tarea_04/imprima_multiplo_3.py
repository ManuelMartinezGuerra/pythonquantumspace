def multiplos_tres():
    contador = 0
    for i in range(int(input('Ingrese un numero : '))):
        if i % 3 == 0 :
            contador += 1
            print(i)
    print(f'la cantidad de multiplo de tres es :{contador} ')
multiplos_tres()
        
