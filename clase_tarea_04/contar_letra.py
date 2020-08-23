frase = input("Ingrese una palabra: ")
letra = input("Ingrese letra que desea contar: ")
cant_letra = 0
for i in frase :
    if i == letra:
        cant_letra = cant_letra + 1
print(f"la letra '{letra}'' se repite  {cant_letra} veces. ")