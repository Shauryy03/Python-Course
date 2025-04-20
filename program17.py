# practice problem
# WAP to ask users to enter names of their 3 favorite movies & store them in a list
# l1 = input("enter your fav movie 1: ")
# l2 = input("enter your fav movie 2: ")
# l3 = input("enter your fav movie 3: ")
# list = []
# list.append(l1)
# list.append(l2)
# list.append(l3)
# print(list)


# WAP to check if a list contain a palindrome element


list1 = [1,2,3,2,1]

tem_list = list1.copy()
tem_list.reverse()

if(list1==tem_list):
    print(True)
else:
    print(False)