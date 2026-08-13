word = input("Enter a word:")
freq = {}
for x in word:
    if x in freq :
        freq[x]+=1
    else:
        freq[x] = 1
print(freq)