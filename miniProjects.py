# #Write a program to input 2 numbers and print their sum

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# sum = num1 + num2
# print("The sum is: " , sum)


# #Write a program to input side of a square and prints its area.

# side_of_square = int(input("Enter length of side: "))
# area = side_of_square * side_of_square
# print("The area of square is: " , area)


# #We can do this by ** operator that means power of
# side_of_square = int(input("Enter length of side: "))
# area = side_of_square ** 2 #This means side_of_square's power 2
# print("The area of square is: " , area)


# #WAP to input 2 floating point numbers and print their average 

# num1 = float(input("Enter num 1: "))
# num2 = float(input("Enter Number 2: "))
# average = (num1 + num2)  / 2
# print(average)


# #WAP to input 2 integer numbers a and b. and
# #Print True if a is greater than or equal to b. otherwise print False.

# num1 = int(input("num 1: "))
# num2 = int(input("num 2: "))
# print(num1 >= num2)


# #WAP to input user's first name and print its length

# first_name = input("Enter your first name: ")
# print("Length of your name is:" , len(first_name))


# #WAP to find the occurance of '$' in  a string

# earning = "I have earned $ 150$"
# print(f"The occurance of '$' is: {earning.count("$")}") #we have to find no of occurances, so use count method


#Grade students based on their marks

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("You score Grade A")
# elif marks >= 80 and marks < 90:
#     print("You score Grade B")
# elif marks >= 70 and marks < 80:
#     print("You score Grade C")
# elif marks <= 70 and marks > 40:
#     print("You score Grade D")
# else:
#     print("You Fail")
    
#OR

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     grade = "A"
# elif marks >= 80 and marks < 90:
#     grade = "B"
# elif marks >= 70 and marks < 80:
#     grade = "C"
# elif marks <= 70 and marks > 40:
#     grade = "D"
# else:
#     grade = "F"
       
# print(f"You have grade {grade} for {marks} marks. ")


# #WAP to check if the number entered by the user is even or odd.

# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")



# #WAP to find the greatest of 3 numbers entered by the user.

# a = int(input("Enter number 1:" ))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3:" ))

# if a >= b and a >= c:
#     print(f"{a} is the largest number.")
# elif b >= a and b >= c:
#     print(f"{b} is the largest number.")
# else:
#     print(f"{c} is the largest number.")


# #WAP to check if a number is a multiple of 7 or not

# number = int(input("Enter a number: "))
# if number % 7 == 0:
#     print("Yes, the number {number} is multiple of 7.")
# else:
#     print("No, the number {number} is not multiple of 7.")


# #WAP to count number of students with grade "A"
# grades = ["C", "D", "A", "A", "B", "B", "A"]
# grades.count("A")
# print(grades)

#WAP to check if a list contain a palindrome of elements or not?

number_list = [1,2,"m",2,1]
name_list = ["mam"]
copy_list = number_list.copy()
number_list1 = copy_list.reverse()
if number_list == copy_list:
    print(f"Yes, {number_list}  is a palindrome")
else:
    print(f"No, {number_list} is not a palindrome.")
