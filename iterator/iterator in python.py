'''An iterator is an object that contains a countable number of values.'''

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)


print(next(myit))
print(next(myit))
print(next(myit))

print("===================")

'''strings '''

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))