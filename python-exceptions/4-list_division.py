#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            num1 = my_list_1[i]
            num2 = my_list_2[i]

            # Attempt division
            try:
                division_result = num1 / num2
            except ZeroDivisionError:
                print("division by 0")
                division_result = 0
            except TypeError:
                print("wrong type")
                division_result = 0

            result.append(division_result)

        except IndexError as e:
            print(e)
            result.append(0)

    return result
