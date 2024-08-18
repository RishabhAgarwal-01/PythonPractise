from numpy import *

arr= array([
    [1,2,3,4],[5,6,7,8]
])
print(arr)
print(arr.ndim) #tells the dimension
print(arr.dtype) #tells the type
print(arr.shape) #tells the number of rows and columns
print(arr.size) #tells the size of array
print(arr[1])
print(arr.flatten()) #flattens the array to 1D

arr2= arr.reshape(2,4) #from 1D to 2D or 3D
print(arr2)
arr3= arr.reshape(2,2,2) #it will create a 3D array having 2 - 2D array and each 2D array having 1D array and each having 2 values
print(arr3)


#creating matrices 
m= matrix(arr)
print(m) 
#or if we have some string then
s='1 2 4 5 7 8 9 4'
m2=matrix(s)
print(m2)
s2='1 2; 4 5; 7 8; 9 4' #this will create a matrix with 4 rows and 2 columns
m3=matrix(s2)
print(m3)

#if we want the diagonal element
s3='1 2 4; 5 7 6; 8 9 4'
m4=matrix(s3)
print(diagonal(m4))

#if max or min
print(m4.max())
print(m4.min())

#we can add 2 matrices but with same mXn value
s4='1 2 4; 5 6 7; 8 9 4'
s5='1 2 4 ;5 7 6;8 9 4'
m5=matrix(s4)
m6=matrix(s5)

m7=m5+m6
print(m7)

#multiplication but it should follow the array compatibility for multiplication
s6='1 2 ;4 5; 6 7; 8 9'
s7='1 2 4 5; 7 6 8 9'
m7=matrix(s6)
m8=matrix(s7)
m9=m7*m8
print(m9)