def bishop_moves(pos) -> int:
    board = [[0] * 8 for _ in range(8)]
    pos_x = pos % 8
    pos_y = pos // 8
    for i in range(8):
        for j in range(8):
            if abs(i - pos_y) == abs(j - pos_x):
                board[i][j] = 1
    bits = ''.join([''.join(map(str, row[::-1])) for row in board[::-1]])
    return int(bits, 2) ^ (1 << pos)
