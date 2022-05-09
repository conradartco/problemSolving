# write a code that takes a string as input and returns the string reversed

reversed_word = ''
give_word = input("Give me a word, any word!: ")

for index in range(len(give_word) -1, -1, -1):
    reversed_word += give_word[index]

print(reversed_word)

# write a code that takes a string as input and capitalize the first letter of each word.
# words will be separated by only one space i.e 'hello world' shoudl be 'Hello World"

user_string = input("Enter phrase to be formatted: ")

result = user_string.title()
print(result)

# a word, phrase, or sequence that reads the same backwards as forward i.e. madam
# write a code that takes a user input and checks to see if it is a palindrome and reports result

get_phrase = input("Enter a palindrome: ")
units = ""
for characters in get_phrase:
    units = characters + units
if (get_phrase == units):
    print(f"Yes, {get_phrase} is a palindrome")
else:
    print("No, that is not a valid palindrome")

# compress a string of characters
# i.e. input of 'aaabbbbbccccaacccbbbaaabbbaaa' would compress to '3a5b4c2a3c3b3a3b3a'

# get user string input
request_string = input("Enter a series of letters in a string: ")

# evaluate user input
def compress(request_string):
    index = 0
    compressed_string = ''
    length_of_input = len(request_string)

# calculate characters in string to compress
    while index != length_of_input:
        current_count = 1
        while (index < length_of_input-1) and (request_string[index] == request_string[index+1]):
            current_count = current_count + 1
            index = index + 1
        if current_count == 1:
            compressed_string += str(request_string[index])
        else:
            compressed_string += str(request_string[index]) + str(current_count)
        index = index + 1
    return compressed_string

print(compress(request_string))