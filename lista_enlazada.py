#La lista enlazada sirve para registrar usuarios
import xml.etree.ElementTree as ET
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

    def modificar(self, name):
        actual = self.primero
        while actual != None and actual.registro.nombre != name:
            actual = actual.siguiente

        #if actual is None:
            #print("No se encontró el usuario con el nombre especificado")
            #return
        print("1. Nombre")
        print("2. Apellido")
        print("3. Teléfono")
        print("4. Correo")
        print("5. Contraseña")
        op = input("Que desea modificar: ")
        if op =="1":
            nombre = input("Nuevo nombre:")
            if actual != None:    
                actual.registro.nombre = nombre

        elif op =="2":
            apellido = input("Nuevo apellido:")
            if actual != None:    
                actual.registro.apellido = apellido
        elif op =="3":
            tel = input("Nuevo teléfono:")
            if actual != None:    
                actual.registro.tel = tel
        elif op =="4":
            correo = input("Nuevo correo:")
            if actual != None:    
                actual.registro.correo = correo
        elif op =="5":
            contra = input("Nuevo contraseña:")
            if actual != None:    
                actual.registro.contra = contra
        else:
            print("Opción inválida")
            return
        tree = ET.parse('gestionarUsuarios.xml')
        root = tree.getroot()

        for usuario in root.findall('usuario'):
            nombre_element = usuario.find('nombre')
            if nombre_element.text == name:
                if op == "1":
                    nombre_element.text = nombre
                elif op == "2":
                    usuario.find('apellido').text = apellido
                elif op == "3":
                    usuario.find('telefono').text = tel
                elif op == "4":
                    usuario.find('correo').text = correo
                elif op == "5":
                    usuario.find('contrasena').text = contra

        # Guardar los cambios en el archivo XML
        tree.write('gestionarUsuarios.xml', encoding="utf-8")

        print("El usuario ha sido modificado correctamente")          

    def buscarAdministrador(self, correo, contra):
        actual = self.primero

        while actual is not None:
            if actual.registro.correo == correo and actual.registro.contra == contra and actual.registro.rol == "administrador":
                return actual.registro

            actual = actual.siguiente

        return None
    
    def buscarCliente(self, correo, contra):

        actual = self.primero

        while actual is not None:
            if actual.registro.correo == correo and actual.registro.contra == contra and actual.registro.rol == "cliente":
                return actual.registro

            actual = actual.siguiente

        return None