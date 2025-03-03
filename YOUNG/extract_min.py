def extract_min(board, m, n):
    if board[0][0] == float('inf'):
        return None

    min_value = board[0][0]
    board[0][0] = board[m-1][n-1]
    board[m-1][n-1] = float('inf')

    def heapify(i, j):
        smallest = i
        if i + 1 < m and board[i + 1][j] < board[smallest][j]:
            smallest = i + 1
        if j + 1 < n and board[i][j + 1] < board[smallest][j]:
            smallest = j + 1

        if smallest != i:
            board[i][j], board[smallest][j] = board[smallest][j], board[i][j]
            heapify(smallest, j)

    heapify(0, 0)
    return min_value
