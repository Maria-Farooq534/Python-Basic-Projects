##User Input

# name = input("Enter your name: ")
# print(f"Welcome {name}")



## print("User input always return string data type even if the value is float or integer!")
# price = input("Enter price: ")
# print(type(price) , price)


# #Multiple inputs with different data types , but results in string
# name = input("Enter Name: ")
# age = input("Enter Age: ")
# marks = input("Enter marks: ")
# print(type(name), name)
# print(type(age) , age)
# print(type(marks) , marks)


#Converting input string type into other data types
name = input("Enter Name: ")
age = int(input("Enter Age: ")) #converting into int
marks = float(input("Enter marks: ")) #converting into float
print(type(name), name)
print(type(age) , age)
print(type(marks) , marks)