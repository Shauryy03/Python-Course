# for loop

# nums = [1,2,3,4,5,6,7,8,9,10]
# for value in nums:
#     print(value)
# else:
#     print("end")

#search for a number x in a tuple using for loop
tup = (1,4,9,16,25,36,49,64,81,100)
x=1000
for value in tup:
    if(value==x):
        print("founded at index",tup.index(value))
        break
else :
    print("not in a tuple")