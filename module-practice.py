# practicing importing and using modules - 

# from random import randint

# # Generate a random number between 1 and 4
# x = randint(1, 4)

# # Define a function to convert numbers to words
# def number_to_word(number):
#     words = ["one", "two", "three", "four"]
#     return words[number - 1]

# # Print the random number as a word
# print(number_to_word(x))


# my own code starts here
# for returning name by number on a dice

from random import randint

# generating a random number between 1 - 6
i = randint(1, 6)

# defining a function to convert numbers to words
def number_to_diceName(dice):
    diceName = ['one', 'two', 'three', 'four', 'five', 'six']
    return diceName[dice -1] # -1 because counting starts from 0

# printing the result of a dice face
if i <= 3:
    print(f'Wow! You got... {number_to_diceName(i)} dice face!')
elif i == 6:
    print(f'SHEESHHH super lucky! You got the ultimate {number_to_diceName(i)} dice face!')
elif i > 3:
    print(f'Gettin lucky, aren\'t you? You got {number_to_diceName(i)} dice face!')
else:
    print('I think we are encountering a problem here... brb.')
