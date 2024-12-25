class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.vin = vin
        self.number = number

        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if  vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)

except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')