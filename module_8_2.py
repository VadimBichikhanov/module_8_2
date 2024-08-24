def personal_sum(numbers):
    """
    Функция для подсчета суммы чисел в коллекции и количества некорректных данных.
    
    :param numbers: Коллекция чисел и/или нечисловых данных.
    :return: Кортеж из двух элементов: сумма чисел и количество некорректных данных.
    """
    result = 0  # Переменная для хранения суммы чисел
    incorrect_data = 0  # Счетчик некорректных данных
    
    for item in numbers:
        try:
            # Попытка преобразовать элемент в число и добавить к сумме
            result += float(item)
        except (TypeError, ValueError):
            # Обработка исключений, если элемент не является числом
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    
    return result, incorrect_data  # Возвращаем кортеж с результатами

def calculate_average(numbers):
    """
    Функция для вычисления среднего арифметического чисел в коллекции.
    
    :param numbers: Коллекция чисел и/или нечисловых данных.
    :return: Среднее арифметическое чисел или 0, если коллекция пуста,
             None, если передан некорректный тип данных.
    """
    try:
        # Если numbers - строка, преобразуем её в список символов
        if isinstance(numbers, str):
            numbers = list(numbers)
        
        # Проверка, является ли numbers коллекцией (список, кортеж или множество)
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError
        
        # Вычисление суммы и количества некорректных данных с помощью personal_sum
        total_sum, incorrect_data = personal_sum(numbers)
        
        # Если количество корректных данных равно 0, возвращаем 0
        if len(numbers) - incorrect_data == 0:
            return 0
        
        # Возвращаем среднее арифметическое корректных данных
        return total_sum / (len(numbers) - incorrect_data)
    
    except TypeError:
        # Обработка исключения, если numbers не является коллекцией
        print('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        # Обработка исключения деления на ноль
        return 0

# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать