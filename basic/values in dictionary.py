car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020
car["color"]="red"

print(x) #after the change





#items ============

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

a = car.items()

print(a) #before the change

car["year"] = 2020

print(a) #

## cheaking if the key is existed..

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
