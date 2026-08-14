word = input("Enter a string: ")
freq = {}
for x in word:
    if x in freq:
        freq[x]+=1
    else:
        freq[x] = 1
found = False
for x in word:
    if freq[x]==1:
        print(x)
        found = True
        break
if not found:
    print("No character with single occurence")
    