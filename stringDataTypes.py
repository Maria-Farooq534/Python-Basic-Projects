name = "My name is Maria"
age = "I am 23 years old"
#Concatenation
Maria = name + age
print(Maria)

a = "a"
b = "b"

c = "a" + " " + "b" # we can print space as well
print(c)

#Escape Sequence Character
c = """
My name is Maria \nI am 23 years old
"""

print(c)

c = """
My name is Maria \tI am 23 years old
"""

print(c)


#Slicing

years = print(age[5:13])
years = print(age[10: len(age)])
#Negative Slicing
year = print(age[-9:-6])