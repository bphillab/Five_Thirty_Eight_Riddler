"""
From Nick Harper comes a question of tempered temperatures:

On a warm, sunny day, Nick glanced at a thermometer, and noticed something quite interesting. When he toggled between
the Fahrenheit and Celsius scales, the digits of the temperature — when rounded to the nearest degree — had switched.
For example, this works for a temperature of 61 degrees Fahrenheit, which corresponds to a temperature of 16 degrees
Celsius.

However, the temperature that day was not 61 degrees Fahrenheit. What was the temperature?
"""

from math import floor, ceil


def convert_C_to_F(C):
    return C * 9 / 5 + 32


def convert_F_to_C(F):
    return (F - 32) * 5 / 9


if __name__ == "__main__":
    for i in range(100):
        f_i_f = floor(convert_C_to_F(i))
        f_i_c = ceil(convert_C_to_F(i))
        i_str = list(str(i))
        i_str.sort()
        f_i_c_str = list(str(f_i_c))
        f_i_c_str.sort()
        f_i_f_str = list(str(f_i_f))
        f_i_f_str.sort()
        if i_str == f_i_c_str or i_str == f_i_f_str:
            print("potential Cel: ", i, " ", convert_C_to_F(i), " ", f_i_f, " ", f_i_c)
