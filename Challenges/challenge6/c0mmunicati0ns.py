with open('input6.txt', 'r') as f:
    f_content = str(f.readlines())  #  apparently I need to convert input into a string

    letter_dict = {}

    for index in range(1,15):
        letter_dict[f'letter{index}'] = ''      #  this creates the dictionary with the 14 letter
                                                #  I thought that doing so manually would be boring
                                                # and that I'd get smarter by not doing so :D

    for index, letter in enumerate(f_content[2:-2], start=1):


        letter_dict['letter1'] = letter_dict['letter2']
        letter_dict['letter2'] = letter_dict['letter3']
        letter_dict['letter3'] = letter_dict['letter4']
        letter_dict['letter4'] = letter_dict['letter5']
        letter_dict['letter5'] = letter_dict['letter6']
        letter_dict['letter6'] = letter_dict['letter7']
        letter_dict['letter7'] = letter_dict['letter8']
        letter_dict['letter8'] = letter_dict['letter9']
        letter_dict['letter9'] = letter_dict['letter10']
        letter_dict['letter10'] = letter_dict['letter11']
        letter_dict['letter11'] = letter_dict['letter12']
        letter_dict['letter12'] = letter_dict['letter13']
        letter_dict['letter13'] = letter_dict['letter14']
        letter_dict['letter14'] = letter

        #  block of code is really messy, but I didn't have a different idea


        #  now I need to check if they're all different, if they are, print the index and we should be done

        checker = []

        for ab in range(1,15):
            checker.append(letter_dict[f'letter{ab}'])


        for letter_checker in range(1,15):
            if letter_dict[f'letter{letter_checker}'] not in checker[letter_checker:15]:
                if letter_checker == 14:
                    print(index)
            else:
                break