def football_points(wins, draws, losses):
    return wins*3 + draws


e = football_points(3, 4, 2)
print(e)
e = football_points(5, 0, 2)
print(e)
e = football_points(0, 0, 1)
print(e)