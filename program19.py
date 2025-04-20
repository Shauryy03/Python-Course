student = {
    "name" : "Saurabh Patel",
    "score" : {
        "chem" : 89,
        "phy" : 90,
        "math" : 96,
    }
}
# print(student["score"])
# print(type(student["score"]))

# print(student["score"]["chem"])
# student["score"]["english"] = 90
# print(student["score"])

print(student.keys())
print(student.values())

# float(6) this is for typecate

print(list(student.keys()))   #type caste krke list ke fomate me store karaya h
print(list(student.values()))
print(len(student))  #length = nummbers of key value

print(student.items())  #retun all (key,values) as atuple
print(list(student.items())) #typecaste 

print(student.get("name")) # return the value of key

student.update({"city" : "shahdol"})
print(student)