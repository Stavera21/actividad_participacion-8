from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    
    # Defina metodo inicializador
    def __init__(self, isbn:str):
        super().__init__(f"El libro con el isb {isbn} esta agotado")
    
    # Defina metodo especial
    def __str__(self):
        return f"El libro con el titulo {self.libro.titulo} y isbn {self.libro.isbn} esta agotado"

    
