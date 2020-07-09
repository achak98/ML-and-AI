def heuristic1(xcoor, ycoor, dim, free_table):

    x = xcoor
    y = ycoor
    score = 0
    present_free_state = free_table

    while(x >= 0):
        while(y >= 0):
            if(present_free_state[x][y] == 0):
                present_free_state[x][y] = 1
                score += 1
            x -= 1
            y -= 1
        break

    x = xcoor
    y = ycoor
    while(x < dim):
        while(y < dim):
            if(present_free_state[x][y] == 0):
                present_free_state[x][y] = 1
                score += 1
            x += 1
            y += 1
        break

    x = xcoor
    y = ycoor
    for i in range(dim):
        if(present_free_state[x][i] == 0):
                present_free_state[x][i] = 1
                score += 1
        if(present_free_state[i][y] == 0):
                present_free_state[i][y] = 1
                score += 1

    return score, present_free_state


def heuristic2(prev_x, prev_y, xcoor, ycoor):
    if(prev_x == -1 and prev_y == -1):
        return 0
    return abs(prev_x-xcoor)+abs(prev_y-ycoor)

def printSolution(board):
    for i in range(dim):
        for j in range(dim):
            print(board[i][j], end=" ")
        print()

def solveNQUtil(board, free_table, col, prev_x, prev_y):

    if col >= dim:
        return True

    scoreList = [[0 for i in range(dim)] for j in range(3)]
    temp = free_table
    for i in range(dim):
            h1_score, temp = heuristic1(i, col, dim, free_table)
            score = h1_score + heuristic2(prev_x, prev_y, i, col)
            scoreList[0].append(score)
            scoreList[1].append(temp)
            scoreList[2].append(i)
    scoreList.sort(key=lambda x: x[0])
    
    for i in range(dim):
        x = scoreList[2][i]
        if free_table[x][col] == 0:
            
            board[i][col] = 1
            free_table = temp
            
            if solveNQUtil(board, free_table, col + 1, x, col) == True:
                return True
                
            board[x][col] = 0


    return False

def solveNQ():
    global dim
    dim = int(input("Enter size of board: "))
    board = [[0 for i in range(dim)] for j in range(dim)]
    free_table = [[0 for i in range(dim)] for j in range(dim)]
    if solveNQUtil(board, free_table, 0, -1, -1) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

solveNQ()
