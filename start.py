import math
LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    try:
        while True:
            try:
                a = int(input('Введите первое число: '))
                b = int(input('Введите второе число: '))
                if a not in LIST or b not in LIST:
                    print()
                break
            except ValueError:
                print('Оно не уметь вычислять Буква -_-')

        print('Выберите действие: (/, *, +, -, //, %, **)')
        print('Выберите действие: (==, !=, >, <, >=, <=)')
        print('Выберите действие: (&, |, ^, ~, >>, <<)')
        c = input('Ваше действие: ')
        #Арифметические операторы
        if c == '/' and b!=0:
            print('Ответ: ', a / b)
        elif c == '*':
            print('Ответ: ', a * b)
        elif c == '+':
            print('Ответ: ', a + b)
        elif c == '-':
            print('Ответ: ', a - b)
        elif c == '//' and b!=0:
            print('Ответ: ', a // b)
        elif c == '%' and b!=0:
            print('Ответ: ', a % b)
        elif c == '**':
            print('Ответ: ', a ** b)
        elif b == 0:
            print('Чел на 0 делить нельзя -_-')
        #Операторы сравнения
        elif c == '==':
            print('Ответ: ', a == b)
            print('Поздравляю они тождественны!')
        elif c != '==':
            print('Печалька, они не тождественны :)')
        if c == '!=':
            print('Ответ: ', a != b)
        elif c == '>':
            print('Ответ: ', a > b)
        elif c == '<':
            print('Ответ: ', a < b)
        elif c == '>=':
            print('Ответ: ', a >= b)
        elif c == '<=':
            print('Ответ: ', a <= b)
        #Побитовые операторы
        elif c == '&':
            print('Ответ: ', a & b)
        elif c == '|':
            print('Ответ: ', a | b)
        elif c == '^':
            print('Ответ: ', a ^ b)
        elif c == '>>':
            print('Ответ: ', a >> b)
        elif c == '<<':
            print('Ответ: ', a << b)
        elif c == '~':
            print('Ответ: ', ~ b)
    except ():
        print()
        break