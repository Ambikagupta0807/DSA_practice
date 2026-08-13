#differnece between largest and smaleest
import array
arr = array.array("i", [])
n = int(input("Enter the no. of elements you want to store in the array: "))
for i in range(n):
    arr.append(int(input("Enter the elements: ")))
print("The array is: ")
print("\n")
for i in range(n):
    print(arr[i], end = " ")
print("\n")
min = arr[0]
for i in range(1,n):
    if arr[i]<min:
        min = arr[i]
        i = i+1
print("smallest element is : ",min)
print("\n")
max=arr[0]
for i in range (1,n):
    if arr[i]>max:
        max = arr[i]
        i = i+1
print("Laregest element is : ", max)
print("\n")
dif = max-min
print("The difference bewteen largest and smaleest element is: ", dif)