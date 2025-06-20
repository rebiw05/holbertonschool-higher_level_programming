#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    differs = []
    for i in set_1:
        if i not in set_2:
            differs.append(i)
    return differs
