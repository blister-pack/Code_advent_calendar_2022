with open('input6.txt', 'r') as f:
    f_content = str(f.readlines())  #  apparently I need to convert input into a string
    letter4 = ''
    letter3 = ''
    letter2 = ''
    letter1 = ''

    for index, letter in enumerate(f_content[2:-2], start=1):

        letter1 = letter2
        letter2 = letter3
        letter3 = letter4
        letter4 = letter

        #  now I need to check if they're all different, if they are, print the index and we should be done

        checker = [letter1, letter2, letter3, letter4]


        if letter1 not in checker[1:4] :
            a = checker[1:4]
            if letter2 not in checker[2:4]:
                b = checker[2:4]
                if letter3 not in checker[3] :
                    c = checker[3]
                    print(index)

    #  answer is printed after printing 3, and it prints all subsequent lines that have the same conditions
    
