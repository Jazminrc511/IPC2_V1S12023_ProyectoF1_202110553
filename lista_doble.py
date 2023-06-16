#La lista de los cines
from nodo import Nodo
import xml.etree.ElementTree as ET
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
  
  def modificar(self, asientos):
    actual = self.primero
    while actual != None and actual.registro.asientos != asientos:
        actual = actual.siguiente
    #print("\n¿Qué desea editar?")
    print("\n")
    print("1. Nombre Cine")
    print("2. Numero de sala")
    print("3. Asiento")
    op = input("Que desea modificar: ")
    if op =="1":
        nombre = input("Nuevo nombre: ")
        if actual != None:    
            actual.registro.nombre = nombre
    elif op =="2":
        sala = input("Nuevo número de sala: ")
        if actual != None:    
            actual.registro.numero = sala
    elif op =="3":
        num = input("Nuevo asientos: ")
        if actual != None:    
            actual.registro.asientos = num
    else:
        print("Opción inválida")
        return
    tree = ET.parse('cine.xml')
    root = tree.getroot()

    tree = ET.parse('cine.xml')
    root = tree.getroot()

    for cine in root.findall('cine'):
        for sala in cine.findall('.//sala'):
            if sala.find('asientos').text == asientos:
                if op == "1":
                    cine.find('nombre').text = nombre
                elif op == "2":
                    sala.find('numero').text = sala
                elif op == "3":
                    sala.find('asientos').text = num
        tree.write('cine.xml', encoding="utf-8")

    print("El cine ha sido modificado correctamente")