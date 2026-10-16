'''Iterator methods are == __iter__()  &   __next__()  
for initialize = __init__()
'''

class MyNumbers: 
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
          x = self.a 
          self.a +=1
          return x


myclass = MyNumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))