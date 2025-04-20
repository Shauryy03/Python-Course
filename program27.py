# WAP to print length of a list
# def leng(l):
#     return len(l)
# print(leng([2,3,4,5]))


# WAP to print factorial
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f 
# print(fact(3))


# WAP to print element of list in single line
# l=[1,2,3,4,5]
# def pri_li(list):
#     for i in list:
#         print(i,end=" ")
  
# pri_li(l)


# WAP to convert USD in INR
# def usd2inr(u):
#     print(u,"$ = ",u*80,"INR")

# usd2inr(int(input("enter the dorllar :")))



def check(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

check(int(input("enter the number : ")))
      