fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#List Comprehension offers the shortest syntax for looping through lists

#Syntax: newlist = [expression for item in iterable if condition == True]

#newlist = ['hello' for x in fruits] - Set all values in the new list to 'hello'

