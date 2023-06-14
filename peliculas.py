class Peliculas:
    def __init__(self, nombre, titulo, director, anio, fecha, hora):
        self.nombre = nombre
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
    def imprimir(self):
    #print(self.codigo)
    #print(self.nombre)
    #print(self.edad)
    #print(self.encargado)
    #print(self.raza)

        print(f"Género: {self.nombre} | Título: {self.titulo} | Director: {self.director} | Año: {self.anio} | Fecha: {self.fecha} | Hora: {self.hora}\n") 


    def imprimirPelis(self):
        print(f"Película: {self.titulo} | Categoría: {self.nombre}\n")

    def Favoritas(self):
        print(f"Película: {self.titulo}\n")