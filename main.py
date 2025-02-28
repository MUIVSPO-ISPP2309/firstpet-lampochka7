import random

def chaslo(min_value, max_value):
    return random.randint(min_value, max_value)

def mnogochaslo(min_value, max_value, count):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_value, max_value))
    return numbers


def generate_unique_random_numbers(min_value, max_value, count):
    if count > (max_value - min_value + 1):
        print("Количество чисел превышает доступный диапазон уникальных значений.")
        return []
    return random.sample(range(min_value, max_value + 1), count)

if __name__ == "__main__":
    min_value = int(input("Введите минимальное значение: "))
    max_value = int(input("Введите максимальное значение: "))

    print("Случайное число:", chaslo(min_value, max_value))

    count = int(input("Введите количество чисел для генерации: "))
    print("Случайные числа:", mnogochaslo(min_value, max_value, count))