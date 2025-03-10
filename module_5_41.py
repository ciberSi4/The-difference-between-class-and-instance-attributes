# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if cls.houses_history is None:
            cls.houses_history = args[0]
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.houses_history = self.houses_history.append(name)

    def __del__(self):
        return print(f"{self.name} снесён, но он останется в истории")


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