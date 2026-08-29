a = 10
b = 20
big = a if a>b else b
print("bigger is", big)

#multiple condition

a = 300
b = 330
print("A") if a>b else print("=") if a == b else print("B")

#default value

username = input()
display_name = username if username else "guest"
print("Welcome,", display_name)