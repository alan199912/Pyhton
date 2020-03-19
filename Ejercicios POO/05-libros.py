# Queremos mantener una coleccion de los libros que hemos ido leyendo,
# poniendoles una calificacion segun nos haya gustado mas o menos al leerlo.
# Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, el
# numero de paginas y la calificacion que le damos entre 0 y 10.

class Libros:

    lista = []

    def __init__(self, titulo, autor, num_pag, clasificacion):
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag
        self.clasificacion = clasificacion

    # agrega a la lista
    def agregar(self, titulo):
        array = []
        if self.titulo == titulo:
            array.append(self.titulo)
            array.append(self.autor)
            array.append(self.num_pag)
            array.append(self.clasificacion)

            self.lista.append(array)

            return print("Agregado")
        else:
            return print("No se agrego")

    # imprime la lista
    def ver(self):
        for i in self.lista:
            print(i)

    # modifica en la lista segun titulo
    def modificarTitulo(self, seleccionar, modificacion):
        if self.titulo == seleccionar:
            for i in self.lista:
                if i[0] == seleccionar:
                    i[0] = modificacion
            return print("Se ha modificado el libro {seleccionar} por {modificacion}".format(seleccionar = seleccionar, modificacion = modificacion))
        else:
            return print("No se pudo modificar porque no se ha encontrado en la lista")
                    
    # elimina segun titulo
    def eliminarLibros(self, seleccionar):
        if self.titulo == seleccionar:
            for i in self.lista:
                if i[0] == self.titulo:
                    self.lista.remove(i)
            return print("Se ha eliminado el libro cuyo titulo era {self.titulo}".format(self = self))
        else:
            return print("No se pudo eliminar porque no se ha encontrado en la lista")

    # busca el mayor puntaje
    def mayorClasificacion(self):
        clasificacion_mayor = 0
        titulo_mayor = ""
        for i in self.lista:
            if i[3] > clasificacion_mayor:
                clasificacion_mayor = i[3]
                titulo_mayor = i[0]
        return print("El que mas puntaje tiene es: {titulo_mayor} con {clasificacion_mayor}".format(titulo_mayor = titulo_mayor, clasificacion_mayor = clasificacion_mayor))

    # busca el menor puntaje
    def menorClasificacion(self):
        clasificacion_menor = 999
        titulo_menor = ""
        for i in self.lista:
            if i[3] < clasificacion_menor:
                clasificacion_menor = i[3]
                titulo_menor = i[0]
        return print("El que menos puntaje tiene es: {titulo_menor} con {clasificacion_menor}".format(titulo_menor = titulo_menor, clasificacion_menor = clasificacion_menor))


# instancia

book = Libros("Libro 1","Edgar Allan Poe",300, 8)
book2 = Libros("Libro 2","Alan",800, 10)
book3 = Libros("Libro 3","no se",123,5)

# agrego con metodo agregar
book.agregar("Libro 1")
book2.agregar("Libro 2")
book3.agregar("Libro 3")

# uso el metodo eliminar para eliminar el 'libro 2'
book2.eliminarLibros("Libro 2")

# uso el metodo modificar el nombre del 'libro 1' por 'primer libro'
book.modificarTitulo("Libro 1","Primer Libro")

# veo todos los libros (no importa por quien use el metodo)
book.ver()

# veo el mayor puntaje (no importa por quien use el metodo)
book3.mayorClasificacion()

# veo el menor puntaje (no importa por quien use el metodo)
book.menorClasificacion()