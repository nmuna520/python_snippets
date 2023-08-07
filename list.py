"""Different ways to copy elements from one list to another."""

list1 = ['a'] * 100000000
def function (list):
    new_list = []
    for i in list:
        new_list.append(i)

def function2 (list):
    new_list = []
    append = new_list.append
    for x in list:
        append(x)

new_list = [x for x in list1]

new_list = list1.copy()


# For copy matrix
import copy
l = [0,1,[2,3]]
l_deepcopy = copy.deepcopy(l)