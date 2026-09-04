temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# now the function with reusable code:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(int(input("enter the fernheit: "))))
print(fahrenheit_to_celsius(int(input("enter the fernheit: "))))
print(fahrenheit_to_celsius(int(input("enter the ferenheit: "))))



    