import random


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число.")


def get_valid_range():
    while True:
        min_value = get_integer_input("Введите минимальное значение: ")
        max_value = get_integer_input("Введите максимальное значение: ")

        if min_value <= max_value:
            return min_value, max_value
        else:
            print("Минимальное значение должно быть меньше или равно максимальному.")


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def generate_random_numbers(min_value, max_value, count):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(min_value, max_value))
    return numbers





if __name__ == "__main__":
    min_value, max_value = get_valid_range()
    print("Случайное число:", generate_random_number(min_value, max_value))
    count = get_integer_input("Введите количество чисел для генерации: ")
    print("Случайные числа:", generate_random_numbers(min_value, max_value, count))


