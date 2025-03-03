def insertara(board, m, n, value):
    board[m-1][n-1] = value

    def up(i, j):
        if i > 0 and board[i][j] < board[i-1][j]:
            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
            up(i-1, j)

        if j > 0 and board[i][j] < board[i][j-1]:
            board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
            up(i, j-1)

    up(m-1, n-1)
