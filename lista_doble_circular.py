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


    def eliminar(self, titulo):
        actual = self.cabeza
        anterior = None
        no_encontrado = False
        
        while actual and actual.registro.titulo != titulo:
            anterior = actual
            actual = actual.siguiente
            
            if actual == self.cabeza:
                no_encontrado = True
                print("No encontrado")
                break

        if not no_encontrado:
            if anterior is not None:
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
            else:
                while actual.siguiente != self.cabeza:
                    actual = actual.siguiente
                actual.siguiente = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente
    """
    def eliminar(self, registro):
        actual = self.primero
        anterior = None
        no_encontrado = False
        
        while actual and actual.receta.colegiado != registro and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente
            
            if actual == self.primero:
                no_encontrado = True
                print("No encontrado")
                break

        if not no_encontrado:
            if anterior is not None:
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
            else:
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
    """