print("Enter the day: ")


num = input()

x = "Fri" if num == 7 else "Sat" if num == 1 else "Sun" if num == 2 else "mon" if num == 3 else "tue" if num == 4 else "wed" if num == 5 else "thu"

print(x)