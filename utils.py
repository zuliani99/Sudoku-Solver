def print_board(SBoard):
    for i in range(len(SBoard)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(SBoard[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(SBoard[i][j])
            else:
                print(str(SBoard[i][j]) + " ", end="")