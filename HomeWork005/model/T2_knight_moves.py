def knight_moves(pos: int) -> int:
    pos = 1 << pos
    pos_left = pos & 0xfefefefefefefefe
    pos_right = pos & 0x7f7f7f7f7f7f7f7f

    moves = (
            (pos_left << 10) | (pos << 17) | (pos_right << 15) |
            (pos_left >> 7) | (pos_right << 7) |
            (pos_left >> 15) | (pos >> 17) | (pos_right >> 10))

    return moves & 0xffffffffffffffff
