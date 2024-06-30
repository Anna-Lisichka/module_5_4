class Building:
    total = 0

    def __init__(self):
        self.name = 'Объект №'
        Building.total += 1


for i in range(1, 41):
    building = Building()
    print('Объект № ', i, building)

print(f'Всего {Building.total} обьектов')