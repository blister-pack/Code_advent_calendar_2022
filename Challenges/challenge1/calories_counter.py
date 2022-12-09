file = open('calories.txt', 'r')
read = file.readlines()

calories_onElf = []
totalCals_onElf3 = 0
totalCals_onElf2 = 0
totalCals_onElf1 = 0
top3_elves = [totalCals_onElf1, totalCals_onElf2, totalCals_onElf3]

for line in read:
    if line != '\n':
        calories_onElf.append(int(line[:-1]))  #  it works but appends with '\n' and that's going to ruin the sum, at the end -- solved
                                               #  I slice off the end of what I don't want and append it to the list as an int
    else:
        if sum(calories_onElf) > top3_elves[0]:
            top3_elves[0] = sum(calories_onElf)
            top3_elves = sorted(top3_elves)

print(sum(top3_elves))

#  use sorted function to simply check if value makes the list (compare to 3rd position) then sort each time a value makes the list