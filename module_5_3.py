# Developer - не только разработчик

class house:
    '''Класс создан для виртуального перемещения по этажам жилых комплексов
    при инициализации класс принимает значения:
    name - Наименование жилого комплекса
    number_of_floor - Количество этажей в комплексе
    создаются атрибуты:
    name
    number_of_floor
    содержит методы:
    __str__;
    выводит полное название и количество этажей
    __len__;
    выводит количество этажей
    __add__;
    реализует добавление этажей
    А так же реализуются методы сравнения, возвращающие или Истину, или Ложь, в зависимости от результата
    prov;
    Осуществляет проверку переданных параметров
    возвращает значение int или self в зависимоти от типа переданного параметра или возвращает 1.
    go_to;
    Метод имитирует счетчик в лифте при подъеме до указанного этажа
    при вводе не существующего или этажа меньше первого выводит сообщение
     "Такого этажа не существует"
    '''

    # Документирование класса - это важная часть, иначе забудем что имеется в классе
    def __init__(self, name, number_of_floors):
        self.name = str(name)
        if isinstance(number_of_floors, int):
            self.number_of_floors = number_of_floors
        else:
            print('Неправильный номер этажа')
            self.number_of_floors = 1

    def prov(self, pp):
        if isinstance(pp, int):
            fl = pp
        elif isinstance(pp, house):
            fl = pp
        else:
            print('неправильное значение')
            fl = self.number_of_floors
        return fl

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        name = f'{self.name}  количество этажей :  {self.number_of_floors}'
        return name

    def __add__(self, other):  # iadd аналогичен, но можно и прописать
        fl = self.prov(other)
        self.number_of_floors = self.number_of_floors + fl
        return self

    def __iadd__(self, other):  # iadd аналогичен, но можно и прописать
        fl = self.prov(other)
        self.number_of_floors += fl
        return self

    def __radd__(self, other):
        fl = self.prov(other)
        self.number_of_floors = fl + self.number_of_floors
        return self

    def __eq__(self, other):
        fl = self.prov(other)
        if self.number_of_floors == fl.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        fl = self.prov(other)
        if self.number_of_floors > fl.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        fl = self.prov(other)
        if self.number_of_floors >= fl.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        fl = self.prov(other)
        if self.number_of_floors < fl.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        fl = self.prov(other)
        if self.number_of_floors <= fl.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        fl = self.prov(other)
        if self.number_of_floors != fl.number_of_floors:
            return True
        else:
            return False

    def go_to(self, new_floor):
        floor = self.prov(new_floor)
        if floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for fl in range(1, new_floor + 1):
            print(f'Этаж: {fl}')


print(house.__doc__)

print()

h1 = house('ЖК "Эльбрус"', 10)
h2 = house('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)  # __eq__
h1 += 10  # __iadd__
print(h1)
h2 = 10 + h2  # __radd__
print(h2)
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
