def arrayManipulation(a):
    hashmap = {}
    for i in range(len(a)):
        hashmap[i] = a[i]
    
    b = [0 for _ in range(len(a))]
    for i in range(len(a)):
        b[i] = hashmap.get(i-1,0) + hashmap.get(i,0) + hashmap.get(i+1,0)
    
    return b

a = [4, 0, 1, -2, 3]
print(arrayManipulation(a))