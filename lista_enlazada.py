#La lista enlazada sirve para registrar usuarios
from nodo import Nodo
class Lista_enlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, registro):
        if self.primero is None:
            self.primero =  Nodo(registro = registro)
            return

        actual = self.primero
        while actual.siguiente:
            actual= actual.siguiente
        actual.siguiente = Nodo(registro =registro)

    def recorrer(self):
        actual = self.primero

        while actual != None:
            #print("hola mundo")
            print("Rol: ", actual.registro.rol, "| Nombre: ", actual.registro.nombre, " | Apellido: ", actual.registro.apellido,  "| Teléfono: ", actual.registro.tel, "| Correo: ", actual.registro.correo, "| Contraseña: ", actual.registro.contra)
            #print("Paciente: ", actual.registro.paciente)
            actual =actual.siguiente

    def buscar(self, nombre, contra):
        actual = self.primero

        while actual is not None:
            if actual.registro.nombre == nombre and actual.registro.contra == contra:
                return actual.registro

            actual = actual.siguiente

        return None

    def eliminar(self, nombre, contra):#, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None

        while actual != None and actual.registro.nombre != nombre and actual.registro.contra != contra: # and actual.registro.fecha_cita != fecha_cita and actual.registro.hora_cita != hora_cita:
        # O puede ser solo "while actual
            anterior = actual
            actual = actual.siguiente
            
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None