# recursion
# recursive function
# def show(n):
#     if(n==0):    #this is the condition jo hame infinte time loop chalne se rokti h
#         return    #and this is called base class in python
#     print(n)
#     show(n-1)

# show(5)


# fibonaci series by recurssion
# def fib(n):
#     if (n==1):
#         return 1
#     if (n==0):
#         return 0
#     f= fib(n-2)+fib(n-1)
#     return f

# print(fib(6))


# factorial
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     f=n*fact(n-1)
#     return f
    
# print(fact(2))


# sum of n natural number

# def sum(n):
#     if(n==1):
#         return 1
#     if(n==0):
#         return 0
#     return sum(n-1)+n

# print(sum(6))


# print elements of list through recurssion
def show(list , index=0):
    if(index == len(list)):
        return 
    print(list[index], end=" ")
    show(list,index+1)

print(show(["mango", "apple","banana","grapes"]))



