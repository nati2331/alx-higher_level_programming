#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError):
            print("wrong type" if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)) else "division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
