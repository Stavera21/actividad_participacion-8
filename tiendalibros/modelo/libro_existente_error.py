from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

    # Defina metodo inicializador
    def __init__(self, isbn:str):
        super().__init__(f"El libro con el isbn {isbn} no existe")

    # Defina metodo especial
    def __str__(self):
        return f"el libro con el titulo {self.libro.titulo} y isbn: {self.libro.isbn} ya existe en el catalogo"
    

