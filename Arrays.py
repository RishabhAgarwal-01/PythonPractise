from array import array

arr= array('i',[]) #here the i is the data type which here is the signed int and array is empty for user data but can have that type of data at time of dec;aration
arrDouble = array('d', []) #double type similary many more can be made

n = int(input("Enter the length of the integer array"))
for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)

for i in arr:
  print(i, end=" ")