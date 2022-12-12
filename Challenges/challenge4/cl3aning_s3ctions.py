with open('input4.txt','r') as f:
    f_contents = f.readlines()

    for section_pairs in f_contents:
        areas = section_pairs.partition(',')
        #  how do I save this without the '\n'
        elf1_area = str(areas[0])
        elf2_area = str(areas[2])
        