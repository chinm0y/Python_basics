def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#accessing individual arguments;

def my_function (*args):
    print("type:", type(args))
    print("first argument:", args[0])
    print("second arguments:", args[1])
    print("all arguments:", args)
    
my_function("emil","tobius", "Linus")