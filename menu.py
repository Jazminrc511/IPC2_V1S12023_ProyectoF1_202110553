from lectura import Lectura
from factura import Factura
class Menu:

    def __init__(self) :
        self.lectu = Lectura()
        #self.factura = Factura()
        self.listaFacturas = []
        self.listaFavoritas = []
        self.main()
        #self.comprarBoletos()

    def main(self):
        print("==== MENÚ ====")
        print("1. Iniciar sesión")
        print("2. Registrar")
        print("3. Ver listado de películas")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            self.iniciar_sesion()
        elif opcion == "2":
            self.registrar()
            self.main()
        elif opcion == "3":
            self.menuImprimirPelisMain()
        elif opcion == "4":
            print("Saliendo del programa...")            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            self.main()

    def iniciar_sesion(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Bienvenido de nuevo, Inicia sesión aqui")
        usuario = input("Ingresa tu nombre de usuario: ")
        contrasena = input("Ingresa tu contraseña: ")
        
        if usuario == "administrador" and contrasena == "123":
            print("Inicio sesión como administrador")
            self.menuAdmin()
        elif usuario =="administrador":
            self.menuAdmin()
        elif usuario == "cliente":
            self.menuClientes()
        else:
            print("Nombre de usuario o contraseña incorrectos")
            self.iniciar_sesion()

#Menús Listos
    def registrar(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Has seleccionado la opción Registrar")
        self.lectu.agregarUsuarios()
        # Aquí puedes añadir la lógica para el registro de usuarios

    def menuAdmin(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Menú Administrador")
        print("Que desea realizar")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Categorías y películas")
        print("3. Gestionar Salas:")
        print("4. Gestionar boletos comprados")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            self.gestionarUsuarios()
        elif opcion == "2":
            self.gestionarPeliculas()
        elif opcion == "3":
            self.gestionarSalas()
        elif opcion == "4":
            self.verFacturas()
        elif opcion == "5":
            self.main()            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            self.menuAdmin()

    def menuClientes(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Menú Administrador")
        print("1. Ver Listado de películas")
        print("2. Listado de películas favoritas")
        print("3. Comprar Boletos")
        print("4. Historial de boletos comprados")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            self.verListadoPeliculas()
            self.menuClientes()
        elif opcion == "2":
            self.menuFavoritas()
        elif opcion == "3":
            self.comprarBoletos()
            self.menuClientes()
        elif opcion == "4":
            self.verFacturasClientes()
            self.menuClientes()
        elif opcion == "5":
            self.main()            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            self.menuClientes()

    def gestionarBoletosComprados(self):
        print("Detalles de los boletos comprados\n")
        self.verFacturas()

    def Eliminar(self):
        print("Detalles de los boletos comprados\n")
        #self.verFacturas()
        nombre = input("A nombre de quien la factura: ")
        pelicula = input("Nombre de la pelicula: ")
        self.eliminarFactura(nombre, pelicula)

    def gestionarUsuarios(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Gestionar Usuarios")
        print("Que desea realizar")
        print("1. Crear")
        print("2. Leer")
        print("3. Modidicar")
        print("4. Eliminar")
        print("5. Regresar")
        opcion = input("Selecciona una opción (1-4): ")
        if opcion == "1":
            #Lectura.agregarUsuarios(self)
            self.lectu.agregarUsuarios()
            self.gestionarUsuarios()
        elif opcion == "2":
            self.lectu.lecturaUsuarios()
            self.gestionarUsuarios()
        elif opcion == "4":
            self.lectu.eliminarUsuario()
            self.gestionarUsuarios()
        elif opcion == "5":
            self.menuAdmin()            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

    def gestionarPeliculas(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Menú Gestionar Peliculas")
        print("Que desea realizar")
        print("1. Crear")
        print("2. Leer")
        print("3. Modidicar")
        print("4. Eliminar")
        print("5. Regresar")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            self.lectu.agregarPeliculas()
            self.gestionarPeliculas()
        elif opcion == "2":
            self.lectu.lecturaPeliculas()
            self.gestionarPeliculas()
        elif opcion == "4":
            self.lectu.eliminarPelicula()
            self.gestionarPeliculas()
        elif opcion == "5":
            self.menuAdmin()            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

    def gestionarSalas(self):
        print("\n--------------------------------------------------------------------------------------")
        print("Gestionar Salas")
        print("Que desea realizar")
        print("1. Crear")
        print("2. Leer")
        print("3. Modidicar")
        print("4. Eliminar")
        print("5. Regresar")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            self.lectu.agregarCine()
            self.gestionarSalas()
        elif opcion == "2":
            self.lectu.lecturaCines()
            self.gestionarSalas()
        elif opcion == "4":
            self.lectu.eliminarSalas()
            self.gestionarSalas()
        elif opcion == "5":
            self.menuAdmin()            
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            self.gestionarSalas()

    def imprimir(self):
        print("Escriba los datos de pelicula que desea ver y sus datos personales para su facturación")
        print("--------------------------------------------------------------------------------------")
        print("Nombre de la pelicula que desea ver: ", self.pelicula)
        print("Fecha (Año-Mes-Día): ", self.fecha)
        print("Hora: ", self.hora)
        print("Numero de boletos: ", self.boletos)
        print("Sala: ", self.sala)
        print("Asientos: ", self.asientos)
        print("\nDatos de facturación")
        print("Nombre: ", self.nombre)
        print("NIT: ", self.nit)
        print("Dirección: ", self.direccion)
        print("Total a pagar: ",self.total)
        print("--------------------------------------------------------------------------------------")

    def verListadoPeliculas(self):
        print("1. Ver listado de peliculas con detalles")
        print("2. Ver solo pelicula con su género")
        print("3. Regresar")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            self.lectu.imprimirPeliculasDetalles()
        elif opcion == "2":
            self.lectu.imprimirPeliculas()
        elif opcion == "3":
            self.menuClientes()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            self.verListadoPeliculas()

    def menuImprimirPelisMain(self):
        print("1. Ver listado de peliculas con detalles")
        print("2. Ver solo el nombre de las peliculas con categoria")
        print("3. regresar")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            self.lectu.imprimirPeliculasDetalles()
            self.menuImprimirPelisMain()
        elif opcion == "2":
            self.lectu.imprimirPeliculas()
            self.menuImprimirPelisMain()
        elif opcion == "3":
            self.main()          
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
            self.menuImprimirPelisMain()

    def comprarBoletos(self):
        self.lectu.imprimirPeliculasDetalles()
        print("Escriba los datos de pelicula que desea ver y sus datos personales para su facturación")
        print("--------------------------------------------------------------------------------------")
        namePeli =input("Nombre de la pelicula que desea ver: ")
        fecha = input("Escriba la fecha que desea ver la película (Año-Mes-Día): ")
        hora = input("Hora de la función: ")
        boletos = int(input("Numero de boletos que desea comprar: "))
        self.lectu.imprimirSalas()
        sala = input("Sala: ")
        asientos = input("Asientos: ")
        print("\nDatos de facturación")
        name = input("Nombre: ")
        nit = input("NIT o CF: ")
        direccion = input("Dirección: ")
        factu = Factura(namePeli, fecha, hora, boletos, sala, asientos, name, nit, direccion)
        self.listaFacturas.append(factu)
        print("Total a pagar: ", factu.total)
        print("--------------------------------------------------------------------------------------")
        print("Compra realizada con éxito")
        #self.verFacturas()

    def verFacturas(self):
        if not self.listaFacturas:  # Verificar si la lista está vacía
            print("Aún no se han comprado boletos.")
            self.menuAdmin()
        else:
            print("Facturas realizadas")
            for f in self.listaFacturas:
                f.imprimir()
            self.menuEliminarFactura()

    def verFacturasClientes(self):
        if not self.listaFacturas:  # Verificar si la lista está vacía
            print("Aún no se han comprado boletos.")
        else:
            print("Historial de boletos comprados")
            for f in self.listaFacturas:
                f.imprimirClientes()

    def menuEliminarFactura(self):
        op = input("\nDesea eliminar una factura (s/n): ")
        if op =="s":
            self.Eliminar()
            self.menuAdmin()
        elif op =="n":
            self.menuAdmin()
        else:
            print("Solo escriba s o n")
            self.menuEliminarFactura()
    
    def verFacturas1(self):
        #print("Facturas realizadas")
        for f in self.listaFacturas:
            f.imprimir()
            
    def eliminarFactura(self, nombre, pelicula):
        nombre = nombre.lower().strip()
        pelicula = pelicula.lower().strip()
        encontrada = False
        for f in self.listaFacturas:
            if f.nombre.lower().replace(" ", "") == nombre and f.pelicula.lower().replace(" ", "") == pelicula:
                self.listaFacturas.remove(f)
                encontrada = True
        if encontrada:
            print("Factura cancelada con éxito.")
        else:
            print("No se encontró ninguna factura con los datos proporcionados.")
        #self.verFacturas()

    def menuFavoritas(self):
        print("1. Ver lista de favoritas")
        print("2. Agregar peliculas favoritas")

        op = input("Opción 1, 2 o 3")
        if op == "1":
            self.imprimirFavoritas()
            self.menuClientes()
        elif op == "2":
            self.favoritas()
            self.menuClientes()
        else:
            print("Opción invalida")
            self.menuFavoritas()


    def favoritas(self):
        self.lectu.favs()
        name = input("\nEscriba el nombre de la pelicula que desea agregar: ")
        self.listaFavoritas.append(name)
        print("Pelicula agregada con éxito")
    
    def imprimirFavoritas(self):
        if self.listaFavoritas:
            print("\n--------------------------------------------------------------------------------------")
            print("Lista de películas favoritas:")
            for pelicula in self.listaFavoritas:
                print(pelicula)
        else:
            print("No hay películas favoritas en la lista.")

Menu()