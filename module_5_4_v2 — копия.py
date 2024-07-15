class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        isinstance_ = super(House, cls).__new__(cls)
        return isinstance_

    def __init__(self, house_name, number_of_floors):
        self.house_name = house_name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.house_name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

