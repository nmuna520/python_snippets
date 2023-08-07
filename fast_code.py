# Interchange two vars
a=1
b=2
a,b = b,a # b=1 a=2

# Invert string
"test_string"[::-1]

# Join string list
words = ["hello", "world"]
" ". join(words)

# Create list of ints
arr = [100]*20 # List of 20 ints with value 100

# Merge two dicts
data1 = {"a":1, "b":2}
data2 = {"c":3, "d":4}
d3 = {**data1, **data2} # Merge data1 and data2


#Merge two lists
list1= [1,2,3]
list2= [4,5,6]
list3 = list1.extend(list2)