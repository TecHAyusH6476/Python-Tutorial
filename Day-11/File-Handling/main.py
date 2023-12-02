folder_path = "C:/Users/Ayush singh/Desktop/Eduscient/Day-11/File-Handling/"
file_name = "a.txt"


# absolute path - most of time work
# we dont use "\" should be replaced "/"


# write
# with open(folder_path + file_name, "w") as file:
#     content = file.write("this is updated text")


# read
with open(folder_path + file_name, "r") as file:
    content = file.read()


print(content)
