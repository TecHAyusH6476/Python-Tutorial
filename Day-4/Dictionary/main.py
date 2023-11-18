# A dictionary is set of key-value pairs
# key -> always unique ( just like roll no) (string and int)
# value -> dynamic (string , int , boolean , list , dict)

# declaration
student = {
    "name": "John Wick",
    "age": 23,
    "grade": "B",
    "medals": ["cricket", "football", "e-sports"],
}

student_name = student["name"]
student_age = student["age"]


# type conversion -> dict_keys -> list
keys = list(student.keys())
val = list(student.values())

# print(keys[3])
# print(val)

if "roll_no" in student:
    print(student["roll_no"])
else:
    print("no roll num key found")
