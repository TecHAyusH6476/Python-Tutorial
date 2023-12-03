def read_and_op(filename):
    try:
        with open(filename, "r") as file:
            # read or readline -> return string
            # read line by line and we need to get the numbers
            num1 = int(file.readline())  # convert string to int
            num2 = int(file.readline())  # convert string to int

            res = num1 / num2

    except FileNotFoundError:
        print("File path is wrong or file doesnt exist")

    except ZeroDivisionError:
        print("num2 cant be 0 ")

    else:  # if try block is working perfect
        print("result = ", res)

    finally:
        print("Code works !!!!! maybe")


file_path = "file...path"

read_and_op(file_path)
