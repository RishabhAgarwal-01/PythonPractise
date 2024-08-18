import math as m
list=[]
for i in range(0, 501):
     if i != 0 and i != 1:
      sqrt= m.sqrt(i)
      floor= m.floor(sqrt)
      if sqrt-floor ==0:
         list.append(i)
print(list)
