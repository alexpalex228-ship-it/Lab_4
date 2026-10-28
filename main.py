"""Главный модуль для демонстрации Лабораторной работы № 4 (Вариант 2)."""

from func_tools import (
    factorial_reduce,
    filter_even_numbers,
    log_calls,
    memoize,
    repeat_call,
)


@log_calls
def multiply(a: int, b: int) -> int:
    """Тестовая функция для демонстрации декоратора логирования."""
    return a * b


@memoize
def fibonacci(n: int) -> int:
    """Рекурсивное вычисление числа Фибоначчи с мемоизацией."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@repeat_call(times=3, prefix="REPEAT")
def greet_user(name: str) -> str:
    """Тестовая функция для демонстрации декоратора с параметрами."""
    msg = f"Привет, {name}!"
    print(f"  -> {msg}")
    return msg


def main() -> None:
    print("=== Лабораторная работа № 4. Вариант 2 ===\n")

    # 1. Задание 2 (средняя): Фильтрация чётных чисел
    print("--- 1. Фильтрация чётных чисел (filter + lambda) ---")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
    evens = filter_even_numbers(nums)
    print(f"Исходный список: {nums}")
    print(f"Чётные числа:    {evens}\n")

    # 2. Задание 4 (средняя): Факториал через reduce
    print("--- 2. Факториал через reduce ---")
    num = 6
    print(f"Факториал числа {num}! = {factorial_reduce(num)}\n")

    # 3. Задание 7 (средняя): Декоратор логирования
    print("--- 3. Декоратор логирования вызова функции ---")
    multiply(7, 8)
    print()

    # 4. Задание 2 (повышенная): Мемоизация через декоратор
    print("--- 4. Декоратор мемоизации (кэширование Фибоначчи) ---")
    print(f"Первый вызов fibonacci(6) = {fibonacci(6)}")
    print(f"Повторный вызов fibonacci(6) = {fibonacci(6)}\n")

    # 5. Задание 6 (повышенная): Декоратор с параметрами
    print("--- 5. Декоратор с параметрами ---")
    greet_user("Алексей")


if __name__ == "__main__":
    main()