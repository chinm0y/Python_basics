myfamily ={
    "child1": {
        "name": "emili🥰",
        "year": 2004
    },
    "child2" :{
        "name": "tobias",
        "year": 2007
    },
    "child3" :{
        "name": "linus",
        "year": 2011
    }
}


print(myfamily)

print(myfamily["child2"]["name"])


#loop...........
for x, obj in myfamily.items():
    print(x)
    
    
    #2nd loop
    
    for y in obj:
        print(y + ':', obj[y])
    