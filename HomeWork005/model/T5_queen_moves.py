from .T4_bishop_moves import bishop_moves
from .T3_tower_moves import tower_moves


def queen_moves(pos) -> int:
    moves = bishop_moves(pos) | tower_moves(pos)
    return moves
