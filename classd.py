class Mapping:
    def __init__(self, iterable):
        self.items_list = []   # variables de instanmcia
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method (con esto se logra mantener update original en clase que hereda)

class MappingSubclass(Mapping): # subclase de Mapping
 
    def update(self, keys, values):    # reescribo update
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)    # llamando a self.items_list de arriba