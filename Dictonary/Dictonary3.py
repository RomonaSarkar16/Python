random_dict={
    "Name":"Angela",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.86,
    "Student":True
}

x=random_dict["Cgpa"]
print(x)

# 2 Item access with the `get()` method ---------------->

random_dict={
    "Name":"A",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}
x=random_dict.get("Name")
print(x)

# We can also see the keys of the dictionaries using `keys()` method and similarly values by the `Values()` method

random_dict={
    "Name":"Angela",
    "University":"AIUB",
    "Semester":"7th",
    "Cgpa": 3.90,
    "Student":True
}
print(random_dict.keys()) #execute  the keys of the dictionary
print(random_dict.values()) #execute  the values of the dictionary

# Updating values ---------------------->

random_dict={
    "Name":"O",
    "University":"AIUB",
    "Semester":"5th",
    "Cgpa": 3.90,
    "Student":True
}
print("\nBefore upgrading  :",random_dict["Name"])

random_dict["Name"]="Romona"

print("After upgrading  :",random_dict["Name"])

random_dict.update({"Cgpa":3.93})

# Checking the availibility of a key in dictionary ------>

random_dict={
    "Name":"Angela",
    "University":"AIUB",
    "Semester":"9th",
    "Cgpa": 3.90,
    "Student":True
}

if "Name" in random_dict :
       print("\nGot it")
else:
    print("No such elements available ")