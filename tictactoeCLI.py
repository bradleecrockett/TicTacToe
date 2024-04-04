



# Determine Winner Function from command line tic tac toe
# returns " " for no winner, or "X" or "O" if it finds 3 in a row.
def determine_winner(b):
    # horizontal winner
    for i in [0,3,6]:
        if b[i] != " " and b[i]==b[i+1] and b[i+1] == b[i+2]:
            return b[i]

    # vertical winner
    for i in range(3):
        if b[i] != " " and  b[i]==b[i+3] and b[i+3] == b[i+6]:
            return b[i]

    # diagonal winner
    if (b[0] == b[4] and b[4] == b[8]) or (b[6] == b[4] and b[4] == b[2]):
        return b[4]

    return " "
