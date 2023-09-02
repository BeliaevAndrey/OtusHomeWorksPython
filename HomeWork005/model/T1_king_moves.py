def king_moves(pos: int) -> int:
    pos = 1 << pos
    pos_left = pos & 0xfefefefefefefefe
    pos_right = pos & 0x7f7f7f7f7f7f7f7f

    moves = (
            (pos_left << 7) | (pos << 8) | (pos_right << 9) |
            (pos_left >> 1) | (pos_right << 1) |
            (pos_left >> 9) | (pos >> 8) | (pos_right >> 7))
    return moves & 0xffffffffffffffff
