word = input("Enter the main string: ")
substr = input("Enter the substring: ")
str_len = len(word)
sub_len = len(substr)
count = 0
for i in range(0, str_len - sub_len+1):
    chunk = word[i:i+sub_len]
    if chunk == substr:
        count +=1
print(f"the occurence of {substr} is {count} times")
