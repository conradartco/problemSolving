# happy numbers
# start with any positive integer
# replace this number by the sum of the squares of its digits
# repeat until the number equals 1
# write a method that determines if a number is happy or sad

#start_num = 2
#end_value = True

#while end_value is True:
#    new_num = start_num + pow(start_num, 2)
#    if new_num == 1:
#        print("Happy!")
#        end_value = False
#    else:
#        continue

# could use index values for pulling int values from an input("Enter a number to check if it's happy or sad: ")

given_value = 19
index = 0
is_happy = False
while is_happy is False:
    new_value = (1 * 1) + (9 * 9)
    if new_value > 1:
        new_value = (pow(new_value[0], 2) + pow(new_value[1], 2))
    elif new_value == 1:
        is_happy = True
        print(f"{given_value} is a happy number!")
    else:
        continue




