#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = list(tuple_a)
    tb = list(tuple_b)
    list_t = [0, 0]

    if len(ta) == 0:
        ta = [0, 0]
    elif len(ta) == 1:
        ta.append(0)
    if len(tb) == 0:
        tb = [0, 0]
    elif len(tb) == 1:
        tb.append(0)

    list_t[0] = int(ta[0]) + int(tb[0])
    list_t[1] = int(ta[1]) + int(tb[1])

    return tuple(list_t)
