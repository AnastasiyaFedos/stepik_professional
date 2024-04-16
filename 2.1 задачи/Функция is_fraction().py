"""
Будем считать обыкновенной дробью последовательность из одной или более цифр, за которой следует прямая косая черта /, а затем — последовательность из одной или более цифр, хотя бы одна из которых отлична от нуля (знаменатель не может равняться нулю). Последовательность, представляющая собой обыкновенную дробь, может начинаться с необязательного символа дефиса -.

Реализуйте функцию is_fraction(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой обыкновенную дробь, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_fraction(), но не код, вызывающий ее.
"""

from fractions import Fraction

def is_fraction(string: str) -> bool:
    try:
        return bool(bool(Fraction(string)) + string.find('/'))
    except:
        return False
