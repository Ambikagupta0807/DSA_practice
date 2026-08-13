word = input("Enter a word:")
vow_count = 0
cons_count = 0
vowels = 'aeiou'
for x in word:
    if x in vowels:
        vow_count +=1
    else:
        cons_count +=1
print(f"The count of vowels are: {vow_count}")
print(f"The count of consonants are: {cons_count}")