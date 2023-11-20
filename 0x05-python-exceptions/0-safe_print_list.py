#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_to_print = my_list[:x]
    count = 0

    for element in elements_to_print:
        print("{}".format(element), end="")
        count += 1

    print()
    return (count)
