file = open('letters.txt', 'r')
read = file.readlines()

#  dictionary with letters of the alphabet and their positions

for rucksack in read:
    no_items = len(rucksack) - 1

    pocket1 = rucksack[:(no_items//2)]
    pocket2 = rucksack[no_items//2:no_items]

    #  only works with //, with / Python returns a float and that creates an error


