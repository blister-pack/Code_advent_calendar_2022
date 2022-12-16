stack1 = ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C']
stack2 = ['N', 'V', 'G', 'P', 'H', 'W', 'B']
stack3 = ['F', 'W', 'B', 'J', 'G']
stack4 = ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S']
stack5 = ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H']
stack6 = ['B', 'C', 'W', 'G', 'F', 'S']
stack7 = ['H', 'T', 'P', 'M', 'Q', 'B', 'W']
stack8 = ['F', 'S', 'W', 'T']
stack9 = ['N', 'C', 'R']

with open('input5.txt', 'r') as f:
    f_content = f.readlines()[10:]

    for move_order in f_content:
        supp = move_order.split()
        boxes_to_move = int(supp[1])
        from_stack = globals()[f'stack{supp[3]}']
        to_stack = globals()[f'stack{supp[5]}']


        movedBox = from_stack[-boxes_to_move:len(from_stack)]
        del from_stack[-boxes_to_move:len(from_stack)]
        to_stack.extend(movedBox)

print(f'{stack1[-1]}{stack2[-1]}{stack3[-1]}{stack4[-1]}{stack5[-1]}{stack6[-1]}{stack7[-1]}{stack8[-1]}{stack9[-1]}')