
class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей: {self.floors}'

    def __len__(self):
        return self.floors

    '''def say_info(self):     # можно и с помощью функции
        print(f'hello:{self.name}, floors {self.floors}')'''

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors

    def __add__(self, value):
        return self.floors + value

    def __iadd__(self, value):
        return self.floors + value

    def __radd__(self, value):
        return self.floors + value

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1.name, h1.floors)
print(h2.name, h2.floors)
print(h1)
print(h2)
'''print(h1.floors) # так же можно использовать вместо __len__ , правда не знаю насколько это правильно.
print(h2.floors)'''
print(len(h1))
print(len(h2))
'''h1.say_info()
h2.say_info()'''
print(h1 == h2) # eq
print(h1 < h2) # lt
print(h1 <= h2) # le
print(h1 > h2) #gt
print(h1 >= h2) # ge
print(h1 != h2) # ne
print(h2.__add__(-4))
print(h2.__iadd__(10))
print(h2.__radd__(23))