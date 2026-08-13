from numpy import *
arr = array([1,2,3,4.5,'d']) #heterogeneous array
for i in arr:
    print(i, end = ",")
print("\n")
arr1 = array([1,2,3], float) #it will convert the integer values to float values
for i in arr1:
    print(i, end = ",")

val = linspace(10, 20, 11) #it will create an array of 11 values from 10 to 20
print("\n") 
for i in val:
    print(i, end = ",")

val1 = arange(1, 10, 2) #it will create an array of values from 1 to 10 with a step of 2
print("\n")
for i in val1:
    print(i, end = ",")
    
val2 = logspace(1, 40, 5) #it will create an array of 5 values from 10^1 to 10^40
print("\n") 
for i in val2:
    print(i, end = ",")
    
val3 = zeros(5) #it will create an array of 5 values with all values as 0
print("\n")
for i in val3:
    print(i, end = ",")
    
val4 = full(10,2) #it will create an array of 10 values with all values as 2
print("\n")
for i in val4:
    print(i, end = ",")
print("\n")

#multidimensional array
from numpy import *
zero = array(5)
print(zero)
one = array([1,2,3,4])
print(one)
two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)
three = array([[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]])
print(three)