import string

file = open('letters.txt', 'r')
read = file.readlines()

#  dictionary with letters of the alphabet and their positions

alphabet_lowerAndUpper = string.ascii_lowercase + string.ascii_uppercase

points_and_letters = {}

for number, letter in enumerate(alphabet_lowerAndUpper):
    points_and_letters[letter] = number + 1
    #  created the dict with the alphabet and their respective point values



value_of_items = 0

for number, rucksack in enumerate(read[2::3]):
    rucksack1 = read[number*3]
    rucksack2 = read[number*3+1]
    rucksack3 = read[number*3+2]

    for letter in rucksack1:
        if letter in rucksack2 and letter in rucksack3:
            value_of_items = value_of_items + points_and_letters[letter]
            break

#  in the second part of the challenge I just need to find the common element in all three rucksacks

print(value_of_items)
