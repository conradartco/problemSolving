# a series of numbers where each number is the sum of the two preceeding numbers (fibonacci)
# i.e. 1, 1, 2, 3, 5, 8, etc
# write a method that does the Fibonacci sequence starting at 1

get_val = input("Enter a number to start Fibonacci sequence: ")
num_value = [0]
for sequence in get_val:
    num_value.append(int(sequence))

while int(get_val) > 0:
    incr_val = num_value[0] + num_value[1]
    print(incr_val)
    up_val = incr_val + num_value[0]
    print(up_val)
    num_value = [up_val]
    num_value.append(int(incr_val))

