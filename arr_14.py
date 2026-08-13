# merge two arrays
import array
arr0 = array.array("i", [2,3,4])
arr1 = array.array("i", [5,6,7])
n0 = len(arr0)
n1 = len(arr1)
for i in range (n1):
    arr0.append(arr1[i])
for i in range(len(arr0)):
    print(arr0[i], end = " ")