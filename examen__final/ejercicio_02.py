class Matriz():
    def __init__(self, t):
        self.t = t
    def crear_lista (self):
        matriz=[]
        for x in range(self.t):
            matriz.append(x)
        return matriz
m = Matriz(5)
print(f'Resultado : ',m.crear_lista())