class Factura:
    def __init__(self, pelicula, fecha, hora, boletos, sala, asientos, nombre, nit, direccion) :
        self.pelicula = pelicula
        self.fecha = fecha
        self.hora = hora
        self.boletos = boletos
        self.sala = sala
        self.asientos = asientos
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.total = boletos*42

    def imprimir(self):
        #print("Detalles de su compra")
        print("\n--------------------------------------------------------------------------------------")
        print("Nombre de la pelicula: ", self.pelicula)
        print("Hecha (Año-Mes-Día): ", self.fecha)
        print("Hora: ", self.hora)
        print("Numero de boletos: #USACIPC2_202110553_", self.boletos)
        print("Sala: ", self.sala)
        print("Asientos: ", self.asientos)
        print("\nDatos de facturación")
        print("Nombre: ", self.nombre)
        print("NIT: ", self.nit)
        print("Dirección: ", self.direccion)
        print("Total a pagar: Q",self.total)
        print("--------------------------------------------------------------------------------------")

    def imprimirClientes(self):
        #print("Detalles de su compra")
        print("\n--------------------------------------------------------------------------------------")
        print("Nombre de la pelicula: ", self.pelicula)
        print("Hecha (Año/Mes/Día): ", self.fecha)
        print("Hora: ", self.hora)
        print("Numero de boletos: #USACIPC2_202110553_", self.boletos)
        #print("Sala: ", self.sala)
        print("Asientos: ", self.asientos)     
        #print("\nDatos de facturación")
        #print("Nombre: ", self.nombre)
        #print("NIT: ", self.nit)
        #print("Dirección: ", self.direccion)
        print("Total a pagar: Q",self.total)
        print("--------------------------------------------------------------------------------------")
        