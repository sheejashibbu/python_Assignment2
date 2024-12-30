randomnum_list= [41,8,13,4,1,59,3]
print(randomnum_list)
randomnum_list.extend([5,6,11,52,100])
print(randomnum_list)
import random
for i in range(10):
 print(random.randint(1,9))
address = dict(name = "John", age = 25, country = "Newyork")
print(address)
address.update(phone=1234567890)
print(address)
set1={1,2,3,4,5}
print(set1)
set1.add(6)
print(set1)
set1.remove(3)
print((set1))
tuple1=(1,2,3)
print(tuple1)
print(len(tuple1))