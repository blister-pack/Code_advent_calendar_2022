with open('input4.txt','r') as f:
    f_contents = f.readlines()
    overlap_areas = 0
    for section_pairs in f_contents:
        areas = section_pairs.partition(',')
        #  how do I save this without the '\n'
        elf1_area = areas[0].split('-')
        elf2_area = areas[2][:-1].split('-')



        first_area = range(int(elf1_area[0]), int(elf1_area[1])+1)
        second_area = range(int(elf2_area[0]), int(elf2_area[1])+1)

        if (second_area.start >= first_area.start and second_area.stop <= first_area.stop) or (first_area.start >= second_area.start and first_area.stop <= second_area.stop):
            overlap_areas += 1

print(overlap_areas)
