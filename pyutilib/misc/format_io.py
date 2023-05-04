#  _________________________________________________________________________
#
#  PyUtilib: A Python utility library.
#  Copyright (c) 2008 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  _________________________________________________________________________


def format_float(x, precision=None):
    """
    Format float in a portable manner, standardizing the
    number of digits in the exponent.
    """
    if type(x) is not float:
        raise TypeError(f"Argument {str(x)} is not a float")
    tmp = str(x)
    if "E" not in tmp and "e" not in tmp:
        return tmp
    sign = "+" if "+" in tmp else "-"
    lst = tmp.split(sign)
    if lst[0] == "" and len(lst) >= 2:
        lst[1] = sign + lst[1]
        lst = lst[1:]
    if abs(x) <= 1e-100 or abs(x) >= 1e100:
        return tmp
    #
    # Use a 2-digit exponent
    #
    i = 0
    while lst[1][i] == '0':
        i += 1
    return lst[0] + sign + lst[1][i:]


def format_io(x):
    """
    Filter function for controlling the format of objects
    """
    return format_float(x) if type(x) is float else str(x)
