# file input output 

f = open("D:\Saurabh Python\demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()



# write mode = "w"
f = open("D:\Saurabh Python\demo.txt","w")
f.write("i want to learn python \n 123")   # over write hoga next demo.txt file me
f.close()   #\n -> next line

# "a" -> append mode
f = open("D:\Saurabh Python\demo.txt","a")
f.write("\nhey  here is new line buddy ")   # add to the last next demo.txt file me
f.close()   #\n -> next line
