from nodo import Nodo
import xml.etree.ElementTree as ET
class listaDobleCircular:
    def __init__(self):
        self.cabeza = None
        self.favoritas = []

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

    
    def buscarPorGenero(self, genero):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            nodo_actual = self.cabeza
            while True:
                if nodo_actual.registro.nombre == genero:
                    print(f"\n- {nodo_actual.registro.titulo}")
                nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.cabeza:
                    break
    
    def buscarPornombre(self, name):
        if self.cabeza is None:
            print("La lista está vacía")
        else:
            nodo_actual = self.cabeza
            while True:
                if nodo_actual.registro.titulo == name:
                    print(f"\nGénero: {nodo_actual.registro.nombre} \n Titulo: {nodo_actual.registro.titulo}\n Director: {nodo_actual.registro.director}\n Año: {nodo_actual.registro.anio}\n Fecha: {nodo_actual.registro.fecha}\n Hora: {nodo_actual.registro.hora}")
                nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.cabeza:
                    break
    
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
    
    def agregarPeliculaFavoritas(self, pelicula):
        pelicula_encontrada = None
        nodo_actual = self.cabeza
        while True:
            if nodo_actual.registro.titulo == pelicula:
                pelicula_encontrada = nodo_actual.registro
                break
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        
        if pelicula_encontrada is not None:
            self.favoritas.append(pelicula_encontrada)
            print(f"La película '{pelicula}' ha sido agregada a tu lista nativa de favoritas.")
        else:
            print(f"No se encontró la película '{pelicula}'.")

    def imprimirListaNativa(self):
        if len(self.favoritas) == 0:
            print("Tu lista de peliculas favoritas está vacía.")
        else:
            print("Lista de películas favoritas:")
            for pelicula in self.favoritas:
                print(f"- {pelicula.titulo}\n")

    def modificar(self, name):
        actual = self.cabeza
        while actual != None and actual.registro.titulo != name:
            actual = actual.siguiente
        print("1. Genero")
        print("2. Título")
        print("3. Director")
        print("4. Año")
        print("5. Fecha")
        print("6. Hora")
        op = input("Que desea modificar: ")
        if op =="1":
            genero = input("Nuevo género: ")
            if actual != None:    
                actual.registro.nombre = genero

        elif op =="2":
            titulo = input("Nuevo título: ")
            if actual != None:    
                actual.registro.titulo = titulo
        elif op =="3":
            director = input("Nuevo director: ")
            if actual != None:    
                actual.registro.director = director
        elif op =="4":
            anio = input("Nuevo Año:")
            if actual != None:    
                actual.registro.anio = anio
        elif op =="5":
            fecha = input("Nueva fecha: ")
            if actual != None:    
                actual.registro.fecha = fecha
        elif op =="6":
            hora = input("Nueva hora: ")
            if actual != None:    
                actual.registro.hora = hora
        else:
            print("Opción inválida")
            return
        tree = ET.parse('categorias.xml')
        root = tree.getroot()

        for categoria in root.findall('categoria'):
            for pelicula in categoria.findall('peliculas/pelicula'):
                titulo_element = pelicula.find('titulo')
                if titulo_element.text == name:
                    if op == "1":
                        titulo_element.text = genero
                    elif op == "2":
                        pelicula.find('titulo').text = titulo
                    elif op == "3":
                        pelicula.find('director').text = director
                    elif op == "4":
                        pelicula.find('anio').text = anio
                    elif op == "5":
                        pelicula.find('fecha').text = fecha
                    elif op == "6":
                        pelicula.find('hora').text = hora
        tree.write('categorias.xml', encoding="utf-8")

        print("Los datos de la película han sido actualizados correctamente")
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