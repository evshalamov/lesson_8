
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OopsDivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    devidend = int(input('Введите числитель: '))
    division = int(input('Введите знаменатель: '))
    if not division:
        raise OopsDivisionByZero('На ноль делить нельзя!')
    print(f'Результат {devidend/division}')

except ValueError:
    print('Не корректный ввод.')
except OopsDivisionByZero as error:
    print(error)

