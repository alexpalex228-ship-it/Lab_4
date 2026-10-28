"""Модуль с функциями и декораторами для Лабораторной работы № 4 (Вариант 2)."""

from functools import reduce, wraps
from typing import Any, Callable


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 2 — Отфильтровать чётные числа из списка
# =====================================================================
def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Фильтрует список, оставляя только чётные числа с помощью filter и lambda."""
    return list(filter(lambda x: x % 2 == 0, numbers))


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 4 — Факториал через reduce
# =====================================================================
def factorial_reduce(n: int) -> int:
    """Вычисляет факториал числа n с использованием функции reduce."""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    if n in (0, 1):
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


# =====================================================================
# СРЕДНЯЯ СЛОЖНОСТЬ: Задание 7 — Декоратор для логирования вызова функции
# =====================================================================
def log_calls(func: Callable) -> Callable:
    """Декоратор, выводящий в консоль имя функции, аргументы и результат."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"[LOG] Вызов {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} вернула: {result!r}")
        return result
    return wrapper


# =====================================================================
# ПОВЫШЕННАЯ СЛОЖНОСТЬ: Задание 2 — Мемоизация функции через декоратор
# =====================================================================
def memoize(func: Callable) -> Callable:
    """Декоратор, кэширующий результаты вызовов функции по её аргументам."""
    cache: dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache:
            print(f"[CACHE] Взято из кэша для аргументов {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


# =====================================================================
# ПОВЫШЕННАЯ СЛОЖНОСТЬ: Задание 6 — Декоратор с параметрами
# =====================================================================
def repeat_call(times: int = 1, prefix: str = "RUN") -> Callable:
    """Декоратор с параметрами: выполняет функцию заданное число раз."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_result = None
            for i in range(1, times + 1):
                print(f"[{prefix} #{i}/{times}] Запуск {func.__name__}...")
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator