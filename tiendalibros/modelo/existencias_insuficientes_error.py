from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    
    # Defina metodo inicializador
    def __init__(self, isbn:str, cantidad_a_comprar:int):
        super().__init__(f"El libro con el isbn {isbn} no tiene suficientes existencias")
        self.cantidad_a_comprar = cantidad_a_comprar

    # Defina metodo espcial
    def __str__(self):
        return f"El libro con el titulo {self.libro.titulo} y isbn {self.libro.isbn} no tiene sufientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}"

    
