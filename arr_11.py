# Print Unique Elements
import array
arr = array.array("i",[])
n=int(input("Enter the number of elements:" ))
for i in range(n):
    arr.append(int(input("Enter the element: ")))
for i in range(n):
    print(arr[i], end = " ")
print("\n")
for i in range(n):
    count = 0
    for j in range(n):
        if arr[i]==arr[j]:
            count+=1
    if count ==1:
        print(arr[i])