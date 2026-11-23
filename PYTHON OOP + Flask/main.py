class DataStructuresDemo:
    """Демонстрация list, dict, set, tuple и list comprehension."""

    def run(self):
        # 1. Список из 10 чисел и только чётные через comprehension
        nums = list(range(1, 11))
        even_nums = [number for number in nums if number % 2 == 0]
        print("1. LIST")
        print("Исходный список:", nums)
        print("Чётные числа:", even_nums)

        # 2. Словарь «товар -> цена»: три пары, обновление, items()
        user = {
            "Ноутбук": 75000,
            "Мышь": 1500,
            "Клавиатура": 3500,
        }
        user["Мышь"] = 1800
        print("\n2. DICT")
        print("Товары и цены:")
        for product, price in user.items():
            print(f"{product}: {price} руб.")

        # 3. Множество из списка с дублями и проверка через in
        source_tags = ["python", "flask", "python", "oop", "flask", "sql"]
        tags = set(source_tags)
        print("\n3. SET")
        print("Исходный список:", source_tags)
        print("Множество без дубликатов:", sorted(tags))
        print("'python' есть в множестве:", "python" in tags)
        print("'django' есть в множестве:", "django" in tags)

        # 4. Кортеж координат: попытка изменения и обработка TypeError
        point = (55.7558, 37.6173)
        print("\n4. TUPLE")
        print("Координаты:", point)
        try:
            point[0] = 56.0
        except TypeError as error:
            print("Изменить элемент tuple нельзя:", error)

        # 5. Одинаковая задача циклом и через comprehension
        numbers = [1, 2, 3, 4, 5]
        squares_loop = []
        for number in numbers:
            squares_loop.append(number ** 2)

        squares_comprehension = [number ** 2 for number in numbers]
        print("\n5. ЦИКЛ И LIST COMPREHENSION")
        print("Квадраты через for:", squares_loop)
        print("Квадраты через comprehension:", squares_comprehension)
        print("Результаты совпадают:", squares_loop == squares_comprehension)

        # Проверка для сдачи (имена переменных соответствуют заданию)
        assert isinstance(nums, list)
        assert isinstance(user, dict)
        assert isinstance(tags, set)
        assert isinstance(point, tuple)
        assert even_nums == [2, 4, 6, 8, 10]
        assert len(tags) == 4
        assert squares_loop == squares_comprehension
        print("\nПроверка задания: OK")


if __name__ == "__main__":
    DataStructuresDemo().run()
