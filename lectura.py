import xml.etree.ElementTree as ET
from lista_enlazada import Lista_enlazada
from registro import Registro
from lista_doble import lista_doble
from cine import Cine
from peliculas import Peliculas
from lista_doble_circular import listaDobleCircular
class Lectura:
    def __init__(self) -> None:
        self.Lista_en = Lista_enlazada()
        self.listaDoble = lista_doble()
        self.circular = listaDobleCircular()
        self.lecturaCines()
        self.editarCine()
        """
        self.lecturaUsuarios()
        print("-------------------------------------------------------------------------")
        self.lecturaCines()
        print("Lectura Pelis-------------------------------------------------------------------------")
        self.lecturaPeliculas()
        print("Agregar Persona")
        self.eliminarUsuario()
        #self.iniciarSesion()
        #self.agregarPeliculas()
        #self.eliminarPelicula()
        #self.agregarCine()
        #self.agregarUsuarios()
        """
    def editarCine(self):
        asiento = input("Escriba el numero de asiento del cine que desea editar")
        self.listaDoble.modificar(asiento)
        self.listaDoble.recorrer()
    def editarPelis(self):
        name = input("Escribe el nombre de la película que deseas editar")
        self.circular.modificar(name)
        self.circular.Imprimir_LDC()
    def editarUsuario(self):
        name = input("Escribe el nombre de la persona que deseas editar: ")
        self.Lista_en.modificar(name)
        self.Lista_en.recorrer()
    def iniciarSesionClientes(self, usuario, contra):
        #usuario = input("Usuario: ")
        #contra = input("Contraseña: ")
        self.Lista_en.buscarCliente(usuario, contra)

    def iniciarSesionAdmin(self, usuario, contra):
        self.Lista_en.buscarAdministrador(usuario, contra)
    def lecturaUsuarios(self):
        tree = ET.parse('gestionarUsuarios.xml')
        root = tree.getroot()

        for register in iter(root.findall('usuario')): 
            rol = register.find('rol').text
            nombre = register.find('nombre').text
            apellido = register.find('apellido').text
            tel = register.find('telefono').text
            correo = register.find('correo').text
            contra = register.find('contrasena').text

            objeto = Registro(rol, nombre, apellido, tel, correo, contra)
            self.Lista_en.insertar(objeto)
        self.Lista_en.recorrer()
#Agregar usuarios manualmente y con archivo logrado :)
    def agregarUsuarios(self):
        rol = "cliente"
        #rol = input("Rol: ").strip()
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        tel = input("Teléfono: ").strip()
        correo = input("Correo: ").strip()
        contra = input("Contraseña: ").strip()
        objeto = Registro(rol, nombre, apellido, tel, correo, contra)
        self.Lista_en.insertar(objeto)
        self.Lista_en.recorrer()
        print("Usuario registrado con éxito")
        tree = ET.parse("gestionarUsuarios.xml")
        root = tree.getroot()
        usuario = ET.SubElement(root, "usuario")
        ET.SubElement(usuario, "rol").text = rol
        ET.SubElement(usuario, "nombre").text = nombre
        ET.SubElement(usuario, "apellido").text = apellido
        ET.SubElement(usuario, "telefono").text = tel
        ET.SubElement(usuario, "correo").text = correo
        ET.SubElement(usuario, "contrasena").text = contra

        tree.write("gestionarUsuarios.xml", encoding="utf-8")


    def eliminarUsuario(self):

        nombre = input("Ingresa el nombre del usuario que quieres eliminar: ").strip()
        contra = input("Ingresa la contraseña del usuario que deseas eliminar: ").strip()

        self.Lista_en.eliminar(nombre, contra)
        self.Lista_en.recorrer()
        print("Usuario eliminado con éxito")

        tree = ET.parse("gestionarUsuarios.xml")
        root = tree.getroot()

        # Buscar y eliminar el elemento deseado
        for usuario in root.findall("usuario"):
            if usuario.find("nombre").text.strip() == nombre and usuario.find("contrasena").text.strip() == contra:
                root.remove(usuario)

        tree.write("gestionarUsuarios.xml", encoding="utf-8")

        """
        nombre = input("Ingresa el nombre del usuario que quieres eliminar: ").strip()
        contra = input("Ingresa la contraseña del usuario que deseas eliminar: ").strip()

        self.Lista_en.eliminar(nombre, contra)
        self.Lista_en.recorrer()
        print("Usuario registrado con éxito")
        tree = ET.parse("gestionarUsuarios.xml")
        root = tree.getroot()
        usuario = ET.SubElement(root, "usuario")
        ET.SubElement(usuario, "rol").text 
        ET.SubElement(usuario, "nombre").text
        ET.SubElement(usuario, "apellido").text
        ET.SubElement(usuario, "telefono").text
        ET.SubElement(usuario, "correo").text
        ET.SubElement(usuario, "contrasena").text

        tree.write("gestionarUsuarios.xml", encoding="utf-8")
        """

    def lecturaCines(self):
        tree = ET.parse('cine.xml')
        root = tree.getroot()
        for cine in iter(root.findall('cine')): 
            name = cine.find('nombre').text.strip()
            #print(f"Nombre del cine: {name.strip()}")
        #cine = root.find('cine')
            for sala in cine.findall("salas/sala"):
                numero = sala.find('numero').text.strip()
                asientos = sala.find('asientos').text.strip()
                objeto = Cine(name, numero, asientos)
                self.listaDoble.insertar(objeto)
        self.listaDoble.recorrer()

            #print(f"Numero de sala: {numero.strip()} Asientos: {asientos.strip()} ")
    def imprimirSalas(self):
        self.listaDoble.recorrer()

    #Ya se puede agregar cine con el xml y manualmente :)
    def agregarCine(self):
        name = input("Nombre del cine: ").strip()
        numero = input("Numero: ").strip()
        asientos = input("Asientos: ").strip()
        objeto = Cine(name, numero, asientos)
        self.listaDoble.insertar(objeto)
        self.listaDoble.recorrer()
        print("Cine registrado con éxito")
        tree = ET.parse("cine.xml")
        root = tree.getroot()
        
        cine = ET.SubElement(root, "cine")
        ET.SubElement(cine, "nombre").text = name
        salas = ET.SubElement(cine, "salas")
        sala1 = ET.SubElement(salas, "sala")
        ET.SubElement(sala1, "numero").text = numero
        ET.SubElement(sala1, "asientos").text = asientos


        tree.write("cine.xml", encoding="utf-8")

    def lecturaPeliculas(self):
        tree = ET.parse('categorias.xml')
        root = tree.getroot()
        for categoria in root.findall("categoria"):
            nombre = categoria.find('nombre').text
            #print(f"Nombre: {nombre.strip()}")
            pelicula = categoria.find('peliculas')

            for peli in pelicula.findall('pelicula'):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora = peli.find('hora').text
                #print(titulo)
                #print("-------------------------------------")
                #print(director)
                objeto = Peliculas(nombre, titulo, director, anio, fecha, hora)
                self.circular.add(objeto)
        self.circular.Imprimir_LDC()
                #print(objeto)

    def agregarPeliculas(self):
        name = input("Clasificación de la pelicula: ").strip()
        titulo = input("Titulo de la pelicula: ").strip()
        director = input("Director de la pelicula: ").strip()
        anio = input("Año de la pelicula: ").strip()
        fecha = input("Fecha: ").strip()
        hora = input("Hora: ").strip()
        objeto = Peliculas(name, titulo, director, anio, fecha, hora)
        self.circular.add(objeto)
        self.circular.Imprimir_LDC()
        print("Pelicula registrada con éxito")
        tree = ET.parse("categorias.xml")
        root = tree.getroot()
        
        cat = ET.SubElement(root, "categoria")
        ET.SubElement(cat, "nombre").text = name
        salas = ET.SubElement(cat, "peliculas")
        sala1 = ET.SubElement(salas, "pelicula")
        ET.SubElement(sala1, "titulo").text = titulo
        ET.SubElement(sala1, "director").text = director
        ET.SubElement(sala1, "anio").text = anio
        ET.SubElement(sala1, "fecha").text = fecha
        ET.SubElement(sala1, "hora").text = hora
        tree.write("categorias.xml", encoding="utf-8")


    
    def eliminarPelicula(self):
        nombre = input("Ingresa el nombre de la película que deseas eliminar: ").strip()
        self.circular.eliminar(nombre)
        self.circular.Imprimir_LDC()
        print("Película eliminada con éxito")
        tree = ET.parse("categorias.xml")
        root = tree.getroot()
        for categoria in root.findall("categoria"):
            peliculas = categoria.find("peliculas")
            for pelicula in peliculas.findall("pelicula"):
                titulo = pelicula.find("titulo").text.strip()
                if titulo == nombre:
                    peliculas.remove(pelicula)
        tree.write("categorias.xml", encoding="utf-8")
        """
        nombre = input("Ingresa el nombre de la pelicula que desea eliminar: ").strip()
        self.circular.eliminar(nombre)
        print("----------------------------------------------------")
        self.circular.Imprimir_LDC()
        print("Película eliminada con éxito")
        tree = ET.parse("categorias.xml")
        root = tree.getroot()
        tree.write("categorias.xml", encoding="utf-8")
        """
    def eliminarSalas(self):
        asientos = input("Escriba el numero de asientos que desea eliminar: ")
        self.listaDoble.eliminar(asientos)
        self.listaDoble.recorrer()
        print("Sala eliminada con éxito")
        tree = ET.parse("cine.xml")
        root = tree.getroot()
        for cine in root.findall("cine"):
            salas = cine.find("salas")
            for sala in salas.findall("sala"):
                asientos_sala = sala.find("asientos").text
                if asientos_sala == asientos:
                    salas.remove(sala)
                    break

        tree.write("cine.xml", encoding="utf-8")


    def imprimirPeliculas(self):
        self.circular.Imprimir_solo_pelis()

    def imprimirPeliculasDetalles(self):
        self.circular.Imprimir_LDC()

    def favs(self):
        self.circular.lasFavoritas()
Lectura()