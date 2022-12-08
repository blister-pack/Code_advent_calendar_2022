file = open('calories.txt', 'r')
read = file.readlines()

calories_onElf = []
totalCals_onElf3 = 0
totalCals_onElf2 = 0
totalCals_onElf1 = 0


for line in read:
    if line != '\n':
        calories_onElf.append(int(line[:-1]))  #  it works but appends with '\n' and that's going to ruin the sum, at the end -- solved
                                               #  I slice off the end of what I don't want and append it to the list as an int
    else:
        if sum(calories_onElf) > totalCals_onElf1:
            totalCals_onElf3 = totalCals_onElf2
            totalCals_onElf2 = totalCals_onElf1
            totalCals_onElf1 = sum(calories_onElf)

        elif sum(calories_onElf) > totalCals_onElf2:
            totalCals_onElf3 = totalCals_onElf2
            totalCals_onElf2 = sum(calories_onElf)

        elif sum(calories_onElf) > totalCals_onElf3:
            totalCals_onElf3 = sum(calories_onElf)
        calories_onElf.clear()



print(totalCals_onElf1 + totalCals_onElf2 + totalCals_onElf3)