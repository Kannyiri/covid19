# print("kannyiri")

# fullname = "umar kannyiri"
# age = 21
# married = true
# hobbies = ['football', 'gaming', 'travelling']
# kids = {
#     "paul": "male",
#     "maurice": "male",
#     "ama": "female"
# }

# # print(hobbies)

# if(married == true):
#     print("happy marriage")
# else:
#     print("save the date")

# # function definition
# def sayhello():
#     print("Hello World")

score = 0
num = 3

while(True):
    if(num % 3 == 0):
         response = input("please input a multiple")
         score = score + num
         num = int(response)
    else:
        print("game over,your score: " + str(score))
        break