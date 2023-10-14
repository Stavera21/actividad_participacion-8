from libro import Libro
from carro_compra import CarroCompras
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError


class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn:str, titulo:str, precio:float, existencias:int):
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)
        
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro
    
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro, cantidad_a_comprar):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.isbn)
        
        if cantidad_a_comprar > libro.existencias:
            raise ExistenciasInsuficientesError(libro.isbn, cantidad_a_comprar)
        
        self.carrito.agregar_item(libro, cantidad_a_comprar)

    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)




    

    
    


    

    



