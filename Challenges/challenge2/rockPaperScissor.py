file = open('rockPaperScissor.txt', 'r')
read = file.readlines()

#  A, X = ROCK (1)
#  B, Y = PAPER (2)
#  C, Z = SCISSOR (3)
#  LOSS = 0, DRAW = 3, WIN = 6

win = ['C X', 'A Y', 'B Z']
draw = ['A X', 'B Y', 'C Z']
lose = ['B X', 'C Y', 'A Z' ]

points = {win[0]:7, win[1]:8, win[2]:9,
          draw[0]:4, draw[1]:5, draw[2]:6,
          lose[0]:1, lose[1]:2, lose[2]:3
          }

score = 0

for line in read:
    score = score + points[line[:3]]

print(score)