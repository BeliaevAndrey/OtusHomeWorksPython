def bishop_moves(pos) -> int:
    board = [[0] * 8 for _ in range(8)]
    pos_x = pos & 7     # pos_x = pos % 8
    pos_y = pos >> 3    # pos_y = pos // 8
    for i in range(8):
        for j in range(8):
            if abs(i - pos_y) == abs(j - pos_x):
                board[i][j] = 1
    bits = ''.join([''.join(map(str, row[::-1])) for row in board[::-1]])
    return int(bits, 2) ^ (1 << pos)

# x % 2 = x & 1; x % 4 = x & 3
# let: pos = 17
# then: pos % 8 -> 1
# 17 & (8 - 1) -> 1
#   10001
#  &
#   00111       <- = (8 - 1)
# --------
#   00001
#
# let: pos = 63
# then: pos % 8 -> 7       <- (63 - 56)
#  111111       <- = (2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0)
#  &
#   00111       <- = (8 - 1)
# --------
#  000111
