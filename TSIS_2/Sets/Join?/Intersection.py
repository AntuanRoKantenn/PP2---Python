x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#The intersection_update() method will keep only the items that are present in both sets.

a = {"apple1", "banana1", "cherry1"}
b = {"google1", "microsoft1", "apple1"}

c = a.intersection(b)

print(c)

#The intersection() method will return a new set, that only contains the 
#items that are present in both sets.