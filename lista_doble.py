#La lista de 
from nodo import Nodo
class lista_doble:
  def __init__(self):
    self.primero = None

  def insertar(self,registro):
    if self.primero is None:
      self.primero = Nodo(registro=registro)
    else:
      actual = Nodo(registro=registro, siguiente=self.primero)
      self.primero.anterior = actual 
      self.primero = actual #me faltaba esta linea

  def recorrer(self):
    if self.primero is None:
      return
    actual = self.primero 
    print("Nombre del cine:", actual.registro.nombre, 
            "| Numero de sala: ", actual.registro.numero, 
            "| Asientos disponibles: ", actual.registro.asientos)
    
    while actual.siguiente:
      actual = actual.siguiente
      print("Nombre del cine:", actual.registro.nombre, 
            "| Numero de sala: ", actual.registro.numero, 
            "| Asientos disponibles: ", actual.registro.asientos,)
    
      
  def eliminar(self,asientos):
    actual = self.primero
    while actual:
        if actual.registro.asientos == asientos:
            if actual.anterior:
                if actual.siguiente:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                else:
                    actual.anterior.siguiente = None
            else:
                if actual.siguiente:
                    self.primero = actual.siguiente
                    actual.siguiente.anterior = None
                else:
                    self.primero = None
            return True
        else:
            actual = actual.siguiente
    return False
  