def enc(board, m, n, value):
    i, j = 0, n - 1
    while i < m and j >= 0:
        if board[i][j] == value:
            return True
        elif board[i][j] < value:
            i += 1
        else:
            j -= 1
    return False
