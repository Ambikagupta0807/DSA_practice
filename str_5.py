word1 = input("Enter first string: ")
word2 = input("Enter second string: ")
sorted_1 = sorted(word1)
sorted_2 = sorted(word2)

if len(word1) != len(word2):
    print("not a anagram")
else:  
    sorted_1 = sorted(word1)
    sorted_2 = sorted(word2)

    if sorted_1 == sorted_2:
        print("Yes it is a anagram ")
    else:
        print("No its not anagram")
