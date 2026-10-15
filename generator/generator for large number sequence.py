def large_sequence(n):
    for i in range(n):
        yield i
        
        
        '''this doesn't create a million numbers in memory'''
        
gen = large_sequence(100000)
print(next(gen))
print(next(gen))
print(next(gen))