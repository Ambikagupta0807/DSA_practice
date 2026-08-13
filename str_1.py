word = input("Enter a string: ")
rev = ""
for x in range(len(word)-1, -1, -1):
    rev += word[x]
print(rev)
