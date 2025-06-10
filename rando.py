import random
print(random.random())
print(random.randint(10,50))
print(random.uniform(10,50))
print(random.choices([1,2,3,4,5],k=5))
print(random.choices([1,2,3,4,5],k=3))
print(random.choices([1,2,3,4,5],k=9))
print(random.sample([1,2,3,4,5],k=5))
print(random.sample([1,2,3,4,5],k=3))
#print(random.sample([1,2,3,4,5],k=9)) --without replacement so must be less than size
print(random.shuffle([1,2,3,4,5])) 
random.seed(5)
print(random.randint(1,22))
print(random.randint(1,222))

random.seed(5)
print(random.randint(1,22))
print(random.randint(1,222))