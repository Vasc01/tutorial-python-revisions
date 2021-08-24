from __future__ import print_function
import sys

##################################################################################################
# Python 2.7+
##################################################################################################
def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i


print("g1: ", end=", ")
g1 = gen1()
for x in g1:
    print(x, end=", ")

##################################################################################################
# Python 3.3+
##################################################################################################
# def gen2():
#     yield from "Python"
#     yield from range(5)
#
# print("\ng2: ", end=", ")
# g2 = gen2()
# for x in g2:
#     print(x, end=", ")
# print()

