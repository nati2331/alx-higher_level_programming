#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            result += a ** b / i if i <= a else raise_exception('Too far')
        except Exception:
            result = b + a
            break

    return result

def raise_exception(message):
    raise Exception(message)
