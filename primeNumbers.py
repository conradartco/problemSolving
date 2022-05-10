# a prime number is a number that is only divisible by one and itself
# write a method that prints out all prime numbers between 1 and 100

# Prime Numbers

def get_prime():
    low = 1
    high = 100
    print("Prime numbers between 1 and 100 are: ")
    for nums in range(low, high + 1):
        if nums > 1:
            for value in range(2, nums):
                if (nums % value) == 0:
                    break
            else:
                print(nums)

get_prime()