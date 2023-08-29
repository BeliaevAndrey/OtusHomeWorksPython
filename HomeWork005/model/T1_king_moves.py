def king_moves(pos: int) -> int:
    """Build bit-mask for moves of king-figure"""
    pos = 1 << pos
    pos_left = pos & 0xfefefefefefefefe
    pos_right = pos & 0x7f7f7f7f7f7f7f7f

    moves = (
            (pos_left << 7) | (pos << 8) | (pos_right << 9) |
            (pos_left >> 1) | (pos_right << 1) |
            (pos_left >> 9) | (pos >> 8) | (pos_right >> 7))
    return moves & 0xffffffffffffffff


def count_pop_slow(mask):
    """Count bits population"""
    count = 0
    while mask:
        count += mask & 1
        mask >>= 1
    return count


def count_pop(mask):
    """Count bits population optimized"""
    count = 0
    while mask:
        count += 1
        mask &= mask - 1
    return count
