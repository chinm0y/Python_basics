a = 200
b = 400
if b>a:
    print("b is better")
elif a == b:
    print("a & b equals")
else:
    print("a is big than b ")
    
    
#odd or even

number = int(input("enter the ID last digit: "))
if  number% 2 == 0:
    print("the number is even ")
else:
    print("this is odd")
    
## with strings

username = input("enter your username: ")
if len(username) >0:
    print(f"welcome,{username}")
else:
    print("error: username cannot be empty")
