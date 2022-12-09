file = open('rockPaperScissor.txt', 'r')
read = file.readlines()

#  A, X = ROCK (1)
#  B, Y = PAPER (2)
#  C, Z = SCISSOR (3)
#  LOSS = 0, DRAW = 3, WIN = 6

'''part2
X = LOSE
Y = DRAW
Z = WIN
'''

win = ['C X', 'A Y', 'B Z']
draw = ['A X', 'B Y', 'C Z']
lose = ['B X', 'C Y', 'A Z' ]

points = {win[0]:2, win[1]:3+1, win[2]:6+3,
          draw[0]:3, draw[1]:3+2, draw[2]:6+1,
          lose[0]:1, lose[1]:3+3, lose[2]:6+2
          }
#  I'll keep the lists as being the same, but I will change the value of the results on  the dictionary to match what is expected
#  In this case, the left column will be losses, the middle one draws and the last one will be victories
score = 0

for line in read:
    score = score + points[line[:3]]

print(score)