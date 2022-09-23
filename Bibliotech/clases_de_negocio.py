class socio:
    def __init__(self, dni, tipo, nombre, email, año):
        self.dni = dni
        self.tipo = tipo
        self.nombre = nombre
        self.email = email
        self.año = año

class libro:
    def __init__(self, isnb, titulo, genero, autor, editorial, estado, tipo):
        self.isbn = isnb
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editorial = editorial
        self.estado = estado
        self.tipo = tipo

class articulo:
    def __init__(self, id_articulo, tipo, nombre, marca, estado):
        self.id = id_articulo
        self.tipo = tipo
        self.nombre = nombre
        self.marca = marca
        self.estado = estado

class prestamo:
    def __init__(self, id_prestamo, fecha_creacion, fecha_devolucion, items, dni):
        self.id = id_prestamo
        self.fecha_creacion = fecha_creacion
        self.fecha_devolucion = fecha_devolucion
        self.items = items
        self.dni = dni


    
 