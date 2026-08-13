word = input("Enter a string: ")
seen = set()
result = ""
for x in word:
    if x not in seen:
        result += x
        seen.add(x)
print(result)
    
    