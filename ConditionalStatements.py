# light = "orange"

# if light == "red":
#     print("stop")
# elif light == "green":
#     print("go")
# elif light == "yellow":
#     print("wait")
# else:
#     print("There's no light")

# num = 10
# if num >= 3:
#     print("Number is greater than 3")
# elif num >= 4:
#     print("Number is greater than 4") #In this case, elif will not execute even if it is true


# num = 10
# if num >= 3:
#     print("Number is greater than 3")
# if num >= 4:
#     print("Number is greater than 4") #If condition will executes even if the first one is true


#Nesting
model_accuracy = 97
if (model_accuracy >= 90):
    if (model_accuracy >= 96):
        print("Model is overfitted")
    else:
        print("Model is trained well")
else:
    print("Model is underfitted")