import math

def lookupTable(numbers):
    result = 0
    hashmap = {}
    for i in range(len(numbers)):
        hashmap[i] = numbers[i]
    
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i]+hashmap[j] > 0 and math.log2(numbers[i]+hashmap[j]).is_integer():
                result += 1

    return result


numbers1 = [1, -1, 2, 3]        #5
numbers2 = [2]                  #1
numbers3 = [-2, -1, 0, 1, 2]    #5
print(lookupTable(numbers1))
print(lookupTable(numbers2))
print(lookupTable(numbers3))