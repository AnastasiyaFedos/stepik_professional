"""
Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.

Реализуйте функцию is_integer(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_integer(), но не код, вызывающий ее.
"""

from re import fullmatch

def is_integer(string: str) -> bool:
    return fullmatch(r'^-?\d+$', string) is not None
