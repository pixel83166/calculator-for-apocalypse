def sum_nums(num1, num2):
    result = 0
    try:
        result = float(num1) + float(num2)
    except ValueError:
        print("Функция сложения работает только с числами.")
    finally:
        return result


def sub_nums(num1, num2):
    result = 0
    try:
        result = float(num1) - float(num2)
    except ValueError:
        print("Функция вычитания работает только с числами.")
    finally:
        return result


def multiply_nums(num1, num2):
    result = 0
    try:
        result = float(num1) * float(num2)
    except ValueError:
        print("Функция умножения работает только с числами.")
    finally:
        return result


def divide_nums(num1, num2):
    result = 0
    try:
        result = float(num1) / float(num2)
    except ValueError:
        print("Функция деления работает только с числами.")
    except ZeroDivisionError:
        print("Нельзя делить на ноль.")
    finally:
        return result


print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
choice = input('Введите номер действия: ')
if choice == "1":
    nomer1 = input("Введите первое число: ")
    nomer2 = input("Введите второе число: ")
    print(sum_nums(nomer1, nomer2))
elif choice == "2":
    nomer1 = input("Введите первое число: ")
    nomer2 = input("Введите второе число: ")
    print(sub_nums(nomer1, nomer2))
elif choice == "3":
    nomer1 = input("Введите первое число: ")
    nomer2 = input("Введите второе число: ")
    print(multiply_nums(nomer1, nomer2))
elif choice == "4":
    nomer1 = input("Введите первое число: ")
    nomer2 = input("Введите второе число: ")
    print(divide_nums(nomer1, nomer2))
else:
    print("Такого действия нет.")