from functools import reduce
from Functions import *

nums= [1,2,3,4,5,6,7,8]

#we can define a function using def or 

# isEven= lambda a: a%2==0
# evens = list(filter(isEven,nums))
#or we can do this

evens = list(filter(lambda a: a%2==0,nums))
print(evens)

doubleEvens = list(map(lambda a: a*2, evens))
print(doubleEvens)

# sum= reduce(lambda acc,a: acc+a, doubleEvens)
#or
sum= reduce(lambda a,b: a+b, doubleEvens)
print(sum)

