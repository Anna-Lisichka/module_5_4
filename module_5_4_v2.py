class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.houses_history.append(self.name)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')




    def __eq__(self, other):
        if not isinstance(other, House):
            raise TypeError('Объект не принадлежит классу House')
            pass
        else:
            return self.floors == other.floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError('Число дополнительных этажей должно быть типом int в __add__')
            pass
        else:
            self.floors += value
            return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise TypeError('Число справа не является типом int в __iadd__')
            pass
        else:
            return self.__add__(value)

    def __radd__(self, value):
        if not isinstance(value, int):
            raise TypeError('Число справа не является типом int в __radd__')
            pass
        else:
            return self.__add__(value)

    def __gt__(self, other):
            if not isinstance(other, House):
                raise TypeError('Объект справа не принадлежит классу House в __gt__')
                pass
            else:
                return self.floors > other.floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise TypeError('Объект справа не принадлежит классу House в __gt__')
            pass
        else:
            return self.floors > other.floors

    def __ge__(self, other):
        if not isinstance(other, House):
            raise TypeError('Объект справа не принадлежит классу House в __ge__')
            pass
        else:
            return self.floors >= other.floors

    def __lt__(self, other):
        if not isinstance(other, House):
            raise TypeError('Объект справа не принадлежит классу House в __lt__')
            pass
        else:
            return self.floors < other.floors

    def __le__(self, other):
        if not isinstance(other, House):
            raise TypeError('Объект справа не принадлежит классу House в __le__')
            pass
        return self.floors <= other.floors

    def __ne__(self, other):
        if not isinstance(other, House):
            raise TypeError('Объект справа не принадлежит классу House в __le__')
            pass
        return self.floors != other.floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"


    # def __del__(self):
    #     print(f'{self.name} снесён, но он останется в истории')


# h1 = House('ЖК Эльбрус-old', 10)
# h2 = House('ЖК Акация-old', 20)

h3 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h4 = House('ЖК Акация', 20)
print(House.houses_history)
h5 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h4
del h5

print(House.houses_history)

# print(h1)
# print(h2)
#
# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__



