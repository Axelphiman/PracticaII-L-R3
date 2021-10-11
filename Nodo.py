class Nodo:
    def __init__(self, dato = None, left = None, right = None):
        #El dato es tipo Object; puede ser lo que sea
        self.dato = dato
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.dato)
