from nodo import Nodo

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def add(self, registro):
        nuevo_nodo = Nodo(registro)

        if self.cabeza is None:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior

            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo

            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    
    def Imprimir_LDC(self):
        if self.cabeza is None:
            print("La lista esta vacía")
        
        else:
            nodo_actual = self.cabeza
            #count = 1
            while True:
                nodo_actual.registro.imprimir()
                nodo_actual = nodo_actual.siguiente

                if nodo_actual == self.cabeza:
                    break

    def Imprimir_solo_pelis(self):
        if self.cabeza is None:
            print("La lista esta vacía")
        
        else:
            nodo_actual = self.cabeza
            #count = 1
            while True:
                nodo_actual.registro.imprimirPelis()
                nodo_actual = nodo_actual.siguiente

                if nodo_actual == self.cabeza:
                    break
    
    def lasFavoritas(self):
        if self.cabeza is None:
            print("La lista esta vacía")
        
        else:
            nodo_actual = self.cabeza
            #count = 1
            while True:
                nodo_actual.registro.Favoritas()
                nodo_actual = nodo_actual.siguiente

                if nodo_actual == self.cabeza:
                    break


    def eliminar(self, registro):
        if self.cabeza is None:
            print("La lista está vacía")
            return
        
        nodo_actual = self.cabeza
        nodo_anterior = None
        encontrado = False
        
        while True:
            if nodo_actual.registro == registro:
                # Caso especial: solo hay un nodo en la lista
                if nodo_actual == self.cabeza and nodo_actual.siguiente == self.cabeza:
                    self.cabeza = None
                    break

                # Caso especial: el nodo a eliminar es la cabeza de la lista
                if nodo_actual == self.cabeza:
                    ultimo = self.cabeza.anterior
                    self.cabeza = self.cabeza.siguiente
                    ultimo.siguiente = self.cabeza
                    self.cabeza.anterior = ultimo
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_anterior
                
                encontrado = True
                break
            
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            
            if nodo_actual == self.cabeza:
                break
        
        if encontrado:
            print("Nodo eliminado correctamente")
        else:
            print("Nodo no encontrado en la lista")