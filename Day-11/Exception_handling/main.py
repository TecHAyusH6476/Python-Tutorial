folder_path = "C:/Users/Ayush singh/Desktop/Eduscient/Day-11/Exception_handling/"
file_name = "c.txt"
try:
    with open(folder_path + file_name, "r") as file:
        # read content of file
        str_content = file.read()
        print(str_content)


except FileNotFoundError:
    print("err: File name is wrong")
