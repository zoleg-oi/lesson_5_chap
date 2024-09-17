# Developer - не только разработчик
# немного отклонился от задания, для улучшения читабельности вывода
class house:
    '''Класс создан для виртуального перемещения по этажам жилых комплексов
    при инициализации класс принимает значения:
    name - Наименование жилого комплекса
    number_of_floor - Количество этажей в комплексе
    создаются атрибуты:
    name
    number_of_floor
    содержит методы:
    __str__
    выводит полное название и количество этажей
    __len__
    выводит количество этажей
    go_to
    Метод имитирует счетчик в лифте при подъеме до указанного этажа
    при вводе не существующего или этажа меньше первого выводит сообщение
     "Такого этажа не существует"
    '''

    # Документирование класса - это важная часть, иначе забудем что имеется в классе
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # print(self.name)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        name = f'{self.name}  количество этажей :  {self.number_of_floors}'
        return name

    def go_to(self, new_floor):

        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for fl in range(1, new_floor + 1):
            print(f'Этаж: {fl}')


print(house.__doc__)

print()

h1 = house('ЖК "Эльбрус"', 10)
print(h1)
print(len(h1))

# h1.go_to(5)
print()
h2 = house('ЖК Акация', 20)
print(h2)
print(len(h2))
# h2.go_to(10)
