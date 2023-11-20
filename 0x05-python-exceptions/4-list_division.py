#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(min(list_length, len(my_list_1), len(my_list_2))):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError):
            print("Error: Division not possible")
            div = 0
        finally:
            new_list.append(div)
    return new_list
