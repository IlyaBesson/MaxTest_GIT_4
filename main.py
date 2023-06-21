"""Написать программу, которая считает кол-во символов в заданной строке

abcd

a 1
b 1
c 1
d 1

aabb

a 2
b 2
"""


# def strcounter(s): # O(N*2) ~ O(N)
#     adict = {}
#     for i in s:
#         adict[i] = adict.get(i, 0) + 1
#     for j in adict:
#         print(j, adict[j])


# def strcounter(s): # O(N**2)
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sub_sym == sym:
#                 counter += 1
#         print(sym, counter)


def strcounter(s):  # O(N*M)
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)


strcounter('abc')