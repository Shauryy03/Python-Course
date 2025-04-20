# functions in python
def cal_sum(a,b):
    sum = a+b
    return sum
print(cal_sum(12,67))


# default argument
def cal_pro(a=1,b=1):
    print(a*b)
    return a*a
print(cal_pro())


def cal_pro(a,b=1):
    print(a*b)
    return a*b
print(cal_pro(4))

# this will through us error hame default prameter hamesa last se likhna srt krna h
# def cal_pro(a=1,b):
#     print(a*b)
#     return a*b
# print(cal_pro(4))