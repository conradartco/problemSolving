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

given_value = input("Enter any number, to check if it's happy or sad: ")
num_value = []
for new_func in given_value:
    num_value.append(int(new_func))

new_list = []

while int(given_value) > 0:
    new_value = pow(num_value[0], 2) + pow(num_value[1], 2)
    if new_value in new_list:
        print(f"Sorry! {given_value} is a sad number")
        break
    elif new_value > 1:
        num_value = []
        new_list.append(int(new_value))
        for ints in str(new_value):
            num_value.append(int(ints))
    elif new_value == 1:
        print(f"Great! {given_value} is a happy number!")
        break
    else:
        break




