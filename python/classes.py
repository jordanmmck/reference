class Animal:
    # these are private
    __name = None
    __sound = None

    # constructor
    def __init__(self, name, sound):
        self.__name = name
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_type(self):
        return "Animal"


cat = Animal('Kitty', 'Meeow')
print(cat.get_name())
