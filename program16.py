# tuples in python 

tup=(87,98,99,43,56,99,99)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup.index(99))
print(tup.count(99))
# tup[1]=80                # not allowed in tuple

tup1 = () #empty tuple
print(type(tup1))

tup2 = (1,)  #single value tuple
print(type(tup2),tup2)

tup3=(1)
print(type(tup3))
