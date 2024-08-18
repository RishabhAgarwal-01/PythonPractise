#lists
nums = [24,5,6,"Not the issue"]
print(nums)

nums2=[1,2,46,62]

nums.append(nums2)
print(nums)

nums.remove(24)
print(nums)

#tupple
tup= (3,1,5,6)
print(type(tup))
print(tup)

print(tup.count(89))

#set
set1={1,7}
set2={3,7}
set3= set1.symmetric_difference(set2)
set4= set1.difference(set2)
print(set2.clear())
print(set3)
print(set4)
print(set2)