# loops in python

# count = 1
# while count<=10:
#     print("hellow")
#     count +=1

# i=1
# while i<=10:
#     print(i)
#     i+=1

# multiplication table
# n=int(input("enter the number : "))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1


# print the numbers of follwing list using loops 
# list = [1,4,9,16,25,36,49,64,81,100]

# n=0
# while n<len(list):
#     print(list[n])
#     n+=1

#search for a number x in a tuple
tup = (1,4,9,16,25,36,49,64,81,100)
x=81
indx=0
while indx<len(tup):
    if(tup[indx]==x):
        print("found at index :",indx)
    indx+=1