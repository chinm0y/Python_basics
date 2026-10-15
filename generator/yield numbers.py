def count_up_to(n):
    count = 1
    while count <= n:
        yield count 
        count +=2
        
for num in count_up_to(50):
    print(num)