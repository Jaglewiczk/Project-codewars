from typing import List


def number(lines):
    count = 1
    list = []
    for a in lines:
        list.append(str(count) + ": " + a)
        count += 1
    return list