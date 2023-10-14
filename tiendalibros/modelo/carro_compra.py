from item_compra import ItemCompra

class CarroCompras:
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.item = []
    
    # Defina el metodo agregar_item
    def agregar_item(self, libro, cantidad):
        item_compra = ItemCompra(libro, cantidad)
        self.item.append(item_compra)

    # Defina el metodo calcular_total
    def calcular_total(self):
        total = 0
        for item in self.item:
            subtotal = item.libro * item.cantidad
            total += subtotal
        return total
    
    # Defina el metodo quitar_item
    def quitar_item(self, isbn):
        self.item = [item for item in self.item if item.libro.isbn != isbn]

    

    
    