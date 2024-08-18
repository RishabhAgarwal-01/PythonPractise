from numpy import *

arr1= array([1,2,3,4,5])
arr2= array([6,7,8,9,10])

arr3= arr1 *2
arr4= arr1+2
arr5 = arr3+arr4
print(arr3)
print(arr4)
print(arr5)
print(log(arr5))
print(sqrt(arr5))
print(max(arr5))
print(min(arr5))
print(concatenate([arr1, arr2]))

#not copying but just creating 2 different refernces for the same memory location
arr6= arr1
print(arr6)
print(id(arr1))
print(id(arr6)) #same id suggest that this created 2 different refernces for the same memory address 

#copying the array , shallow copy i.e change in one array's value will be reflected back in other array
arr6= arr1.view()
print(arr6)
print(id(arr1)) #different id i.e references and location are different but change in one array's value will be reflected back in other array
print(id(arr6))
arr1[0]=6
print(arr1)
print(arr6) #changes happened in both i.e they are still dependent on each other

#deep copy, i.e to remove any dependence and change in one will not be reflected in other
arr6= arr1.copy()
print(arr6)
arr1[0]=1
print(arr1)
print(arr6) #no change in the other array