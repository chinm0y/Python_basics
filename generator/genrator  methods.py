def echo_generator():
    while True:
        received = yield
        print("Received:", received)
        
gen = echo_generator()
next(gen) #prime the generator
gen.send("hello")
gen.send("world")
        
        
        
'''Close method'''
        

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")
        
        
gen = my_gen()
print(next(gen))
gen.close()