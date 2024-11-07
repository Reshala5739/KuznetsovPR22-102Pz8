class Soda:
    def __init__(self, addon=None):
        self.addon = addon

    def show_my_drink(self):
        if self.addon:
            print(f"Газировка и {self.addon}")
        else:
            print("Обычная газировка")

drink1 = Soda("банан")
drink1.show_my_drink()

drink2 = Soda()
drink2.show_my_drink()

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not all(isinstance(x, (int, float)) for x in [self.a, self.b, self.c]):
            return "Нужно вводить только числа!"
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."
checker1 = TriangleChecker(3, 4, 5)
print(checker1.is_triangle())

checker2 = TriangleChecker(-1, 2, 3)
print(checker2.is_triangle())

checker3 = TriangleChecker(1, 2, 3)
print(checker3.is_triangle())

checker4 = TriangleChecker(1, 1, 3)
print(checker4.is_triangle())


class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self._kg * 2.205

converter = KgToPounds(5)
print(converter.kg)
print(converter.to_pounds())

converter.kg = 10
print(converter.kg)
print(converter.to_pounds())

class Nikolay:
    def __init__(self, name, age):
        if name == "Николай":
            self._name = name
        else:
            self._name = f"Я не {name}, а Николай"
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    # def __setattr__(self, name, value):
    #     raise AttributeError("Нельзя добавлять новые атрибуты к экземпляру класса Nikolay")

nikolay_1 = Nikolay("Николай", 30)
print(nikolay_1.name)
print(nikolay_1.age)
nikolay_2 = Nikolay("Максим", 25)
print(nikolay_2.name)
print(nikolay_2.age)
try:
    nikolay_1.middle_name = "Николаевич"
except AttributeError as e:
    print(e)

class RealString:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self) == len(other)
        elif isinstance(other, str):
            return len(self) == len(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self) < len(other)
        elif isinstance(other, str):
            return len(self) < len(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self) > len(other)
        elif isinstance(other, str):
            return len(self) > len(other)
        return NotImplemented

string1 = RealString("Apple")
string2 = RealString("Яблоко")
string3 = RealString("Grusha")
print(string1 < string2)
print(string1 > string3)
print(string1 == "Apple")
print(string2 == "Яблоко")
print(string1 == string3)