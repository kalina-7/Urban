class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor <= self.number_of_floors and new_floor >= 1:
            for i in range(new_floor):
                print(i+1)
        else:
            print('"Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('Датский квартал', 17)
h2 = House('Алые паруса', 25)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))