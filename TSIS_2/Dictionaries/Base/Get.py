thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
#Get a list of the key:value pairs
x = thisdict.items()
#checking
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")