with open('input4.txt','r') as f:
    f_contents = f.readlines()
    overlap_areas = 0
    for section_pairs in f_contents:
        areas = section_pairs.partition(',')
        #  how do I save this without the '\n'
        elf1_area = areas[0].split('-')
        elf2_area = areas[2][:-1].split('-')



        first_area = range(int(elf1_area[0]), int(elf1_area[1]))
        second_area = range(int(elf2_area[0]), int(elf2_area[1]))

        if first_area in second_area or second_area in first_area:
            overlap_areas += 1
            #  it's not counting
