import string

file = open('letters.txt', 'r')
read = file.readlines()

#  dictionary with letters of the alphabet and their positions

alphabet_lowerAndUpper = string.ascii_lowercase + string.ascii_uppercase

points_and_letters = {}
for number, letter in enumerate(alphabet_lowerAndUpper):
    points_and_letters[letter] = number + 1
    #  created the dict with the alphabet and their respective point values

for rucksack in read:
    no_items = len(rucksack) - 1

    pocket1 = rucksack[:(no_items//2)]
    pocket2 = rucksack[no_items//2:no_items]

    
    #  only works with //, with / Python returns a float and that creates an error


