# Class item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Dictionary of known items
item_dict = {
    'Pantalone': Item('Pantalone', 1.0),
    'Giacca': Item('Giacca', 1.0),
    'Gonna': Item('Gonna', 1.0),
    'Giubbotto': Item('Giubbotto', 1.0),
    'Giaccone': Item('Giaccone', 1.0),
    'Cappotto': Item('Cappotto', 1.0),
    'Impermeabile': Item('Impermeabile', 1.0),
    'Abito Donna': Item('Abito Donna', 1.0),
    'Maglia': Item('Maglia', 1.0),
    'Maglione': Item('Maglione', 1.0),
    'Camicia': Item('Camicia', 1.0),
    'Tenda': Item('Tenda', 1.0),
    'Tappeto': Item('Tappeto', 1.0),
    'Camicia': Item('Camicia', 1.0),
    'Coperta lana': Item('Coperta lana', 1.0),
    'Coperta leggera': Item('Coperta leggera', 1.0),
    'Trap. matr. sint.': Item('Trap. matr. sint.', 1.0),
    'Trap. matr. piuma': Item('Trap. matr. piuma', 1.0),
    'Trap. sing. sint.': Item('Trap. sing. sint.', 1.0),
    'Trap. sing. piuma': Item('Trap. sing. piuma', 1.0),
    'Coprimaterasso': Item('Coprimaterasso', 1.0),
    'Cuscino': Item('Cuscino', 1.0)
}
