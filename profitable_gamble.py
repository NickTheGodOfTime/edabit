def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        print(True)
    else:
        print(False)


e = profitable_gamble(0.2, 50, 9)
e = profitable_gamble(0.9, 1, 2)
e = profitable_gamble(0.9, 3, 2)