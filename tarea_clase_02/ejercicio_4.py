n1 = int(input("Ingrese un numero: "))

n2 = int(input("Ingrese numero: "))

n3 = int(input("Ingrese  numero: "))

n4 = int(input("Ingrese  numero: "))

if n1>n2>n3>n4:

    print(f"El numero mayor es {n1}")

elif n2 > n1 > n3 > n4:

    print(f"El numero mayor es {n2}")

elif n3 > n2 > n1 > n4:

    print(f"El numero mayor es {n3}")

elif n4 > n3 > n2 > n1:

    print(f"El numero mayor es {n4}")

if n1 < n2 < n3 < n4:

    print(f"El numero menor es {n1}")

elif n2 < n1 < n3 < n4:

    print(f"El numero menor es {n2}")

elif n3 < n2 < n1 < n4:

    print(f"El numero menor es {n3}")

elif n4 < n3 < n2 < n1:

    print(f"El numero menor es {n4}")  