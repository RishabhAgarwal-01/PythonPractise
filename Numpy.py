from numpy import *

#first way of creating arr using numpy // we don't need to mention the type here, but we can if you want
arr= array([1,2,3,4,5,6])
print(arr)
print(arr.dtype)
arr= array([1,2,3,4,5,6.0]) #now all of them will become the float type
print(arr.dtype)
print(arr)

#2nd way using linspace() function
arr2= linspace(1,5,10) #first parameter is start, end range (excluding) and the parts you want to break into
#if not divided then it will take 50 parts by default
print(arr2)


#3rd way using arange function
arr3= arange(1,10,2) #the last parameter is the steps
print(arr3)

#fourth way using the logspace()
arr4= logspace(1,10,5) #create the 5 space but the log value 
print(arr4) 
#if not want in  the natural log power then simply do
print("%.2f" %arr[5])

#fifth one using the zeros() if we want a array with zero as initail value
arr5= zeros(5) #the parameter is the size of array
print(arr5)
#if want the int then
arr6= zeros(5, int)
print(arr6)

#ones()
arr7= ones(5)
print(arr7)