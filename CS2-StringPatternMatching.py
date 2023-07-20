def stringPatternMatching(pattern, source):
    count = 0
    vowels = ['a','e','i','o','u','y']

    for i in range(0,len(source)-3):
        if source[i] in vowels and \
            source[i+1] not in vowels and \
            source[i+2] in vowels:
            count += 1
    return count


# Expected: 2
pattern = "010"
source = "amazing"

print(stringPatternMatching(pattern, source))