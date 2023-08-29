def tower_moves(pos: int) -> int:
    moves = 72340172838076673 << (pos % 8) ^ 255 << (8 * (pos // 8))

    return moves & 0xffffffffffffffff
