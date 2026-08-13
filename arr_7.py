#Count Frequency of a Given Element
import array
arr = array.array("i", [])
n = int(input("Enter the number of elements: "))
for i in range(n):
    arr.append(int(input("Enter elements")))
for i in range(n):
    print(arr[i], end = " ")
print("\n")
num = int(input("Enter the number: "))
freq = 0
if num in arr:
    for i in range(n):
        if arr[i] == num:
            freq = freq+1
else:
    print("number is not present in array")

print("the frequency of number is", freq)
    
    