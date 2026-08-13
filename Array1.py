from array import *
arr = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)

arr1 = array('f', [1, 2, 3, 4, 5, 6, 7, 8, 9.0, 10])
print(arr1)

arr2 = array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(arr2)

for i in range (0,5):
    print(arr[i])
print("\n")
for i in range (0, len(arr)):
    print(arr[i])
print("\n")
for i in arr:
    print(i, end = ",")
    
#typecode it will return the type of data stored in the array
print("\n")
print(arr2.typecode)
print("\n")
#reverse the array
arr1.reverse()
for i in range (0, len(arr1)):
    print(arr1[i], end = ",")
    
print("\n")
#inserting element in the array  
arr.insert(0, 0)
arr.append(11) #add element at the end of the array
arr[3] = 12 #overwrite the value at index 3
print(arr)
print("\n")
#copying the array
copied_arr = array('i', (x for x in arr)) #if we dont the typecode we can write arr.typecode instead of 'i'
#we can also modufy the values in copied array for ex 3x for x in arr it will multiply each element of arr by 3 and store it in copied_arr
for i in range (0, len(copied_arr)):
    print(copied_arr[i], end = ' ' ) # or you can directly print the array without using loop
#deleting the element from the array
arr.pop(0)# it will remove the 0 index element from the array
arr.remove(12) # it will remove the 12 from the array
arr.pop() # it will remove the last element from the array
print("\n") 
for i in arr:
    print(i, end = ",")
print("\n")
# slicing the array
sliced_arr = arr[0:5] # it will slice the array from index 0 to 4
print(sliced_arr)
print("\n")
sliced_arr1 = arr[0:-3]# it will slice the array from starting index to the index which is 3 from the end
print(sliced_arr1)
print("\n")
reversed_arr = arr[::-1] # it will reverse the array
for i in reversed_arr:
    print(i, end = ",")
print("\n") 

#taking values from user for a array
import array
arr = array.array('i', [])
n = int(input("Enter the elements you want to store in the array : "))
for i in range(n):
    arr.append(int(input("Enter next number: ")))
for i in arr:
    print(i, end = ',')
#searching an element in the array by index value
import array


print("\n")
arr1 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
i = arr1.index(7)
print(i)
