class StringArray:
    def __init__(self):
        self.array = []  # массив строк
        self.lengths = []  # массив длин строк

    def add_string(self, s):
        self.array.append(s)  # добавление новой строки в массив
        self.lengths.append(len(s))  # сохранение длины строки

    def get_string(self, idx):
        if idx < 0 or idx >= len(self.array):  # проверка выхода индекса за пределы массива
            print("Error: Index out of range")
            return None
        else:
            return self.array[idx]  # возвращение строки по индексу

    def concat(self, other_array):
        if len(self.array) != len(other_array.array):  # проверка размеров массивов
            print("Error: Different array sizes")
            return None
        else:
            result = StringArray()  # создание нового массива
            for i in range(len(self.array)):
                result.add_string(self.array[i] + other_array.array[i])  # склейка строк и добавление в новый массив
            return result

    def merge(self, other_array):
        result = StringArray()  # создание нового массива
        for i in range(len(self.array)):
            if self.array[i] not in other_array.array:  # проверка на повторяющиеся элементы
                result.add_string(self.array[i])
        for i in range(len(other_array.array)):
            if other_array.array[i] not in self.array:  # проверка на повторяющиеся элементы
                result.add_string(other_array.array[i])
        return result

    def display(self):
        for i in range(len(self.array)):
            print(self.array[i])
        print()  # пустая строка для отступа
arr1 = StringArray()
arr1.add_string("Hello")
arr1.add_string("world")

# Получение элемента массива
print(arr1.get_string(0))

# Создание и заполнение другого массива
arr2 = StringArray()
arr2.add_string("Python")
arr2.add_string("world")

# Сцепление двух массивов
arr3 = arr1.concat(arr2)
arr3.display()

# Слияние двух массивов
arr4 = arr1.merge(arr2)
arr4.display()