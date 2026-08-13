#Find the Second Largest Element
import array
arr = array.array("i", [10,50,20,0,30])
n = len(arr)
for i in range(n):
    print(arr[i], end = " ")
largest = arr[0]
second_largest = arr[0]
for i in range(1, n):
    if(arr[i]>largest):
        second_largest = largest
        largest = arr[i]
        
    elif(arr[i]>second_largest):
        second_largest = arr[i]
        
print("\n")
        
print("the second largest element is: ", second_largest)
    
         
    
