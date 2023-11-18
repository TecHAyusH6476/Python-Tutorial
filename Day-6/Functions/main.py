# functions defnition

# ** return is optional

# Python , Javascript  , Go .. -> Interpreter
# C , C++ , java , kotlin -> compiler


# 1st non parameterized
def greet_world():
    print("hello world!!!")


# greet_world()


# 2nd


# formal params
# def add(a, b):
#     print(a + b)


# # actual params
# # add(12, 23)


# # param with a default value
# def greet(name="sachin!"):
#     print("hello , " + name)


# greet()
# greet("ayush")


# # Function with multiple return values
# def get_location():
#     a = 12
#     b = 34
#     return a, b


# val1, val2 = get_location()


# print(val2)
# print(str(val1) + "hello")


# Function with return type as function


def multiplier(factor):
    def eg():
        print(factor * 12)  # 144

    return eg


a = multiplier(12)
# if a is function a()

a()


# Function can be used only when we call it "add()"
