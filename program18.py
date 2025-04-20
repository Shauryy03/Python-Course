# dictionary in python

info = {
    "name" : "apnacollege",
    "subject" : ["python", "java", "c++"],
    "topic" : ("dict", "set", "list"),
    "age" : 21,
    "is_adult" : True,
    12.99 : 12.99
}

print(info)
print(type(info))

print(info["name"])
print(info["subject"])

info["name"] = "saurabh"
print(info["name"])

info["surname"] = "patel"
print(info['surname'])
