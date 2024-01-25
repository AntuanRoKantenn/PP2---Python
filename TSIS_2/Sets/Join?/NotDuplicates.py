x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#will keep only the elements that are NOT present in both sets
#True and 1 are the same in sets