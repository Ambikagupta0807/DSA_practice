word = input("Enter a string: ")
old = word
rev = ""
for x in range(len(word)-1, -1, -1):
    rev += word[x]
if old == rev:
    print(f"Yes Palindrome: {rev}")
else:
    print(f"Not a palindrome: {rev}")