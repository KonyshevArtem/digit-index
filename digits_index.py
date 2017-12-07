import math

def find_digits_on_index_from_zero(index):
    digits_amount = 1
    bound = 9
    number = 0
    while index > bound:
        number += bound
        index -= bound
        bound *= 10
        digits_amount += 1
    offset = math.ceil(index / digits_amount)
    number += offset
    return int(str(number)[digits_amount - 1 - (digits_amount * offset - index)])

def find_digits_on_index_from_one(index):
    return find_digits_on_index_from_zero(index + 1)