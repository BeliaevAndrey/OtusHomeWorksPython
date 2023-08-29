def knight_moves(pos: int) -> int:
    pos = 1 << pos
    pos_lft_cut_1 = 0xfefefefefefefefe          # cut edge (a)
    pos_lft_cut_2 = 0xFcFcFcFcFcFcFcFc          # cut edge-1 (a b)
    pos_rgt_cut_1 = 0x7f7f7f7f7f7f7f7f          # cut edge (h)
    pos_rgt_cut_2 = 0x3f3f3f3f3f3f3f3f          # cut edge-1 (g h)

    moves = pos_lft_cut_2 & (pos << 10)         # shift:  1 down 2 left ; and: cut a b
    moves |= pos_lft_cut_1 & (pos << 17)        # shift:  2 down 1 left ; and: cut a
    moves |= pos_rgt_cut_1 & (pos << 15)        # shift:  2 down 1 right; and: cut h
    moves |= pos_rgt_cut_2 & (pos << 6)         # shift:  1 down 2 right; and: cut g h

    moves |= pos_lft_cut_2 & (pos >> 6)         # shift:  1 up 2 left ; and: cut a b
    moves |= pos_lft_cut_1 & (pos >> 15)        # shift:  2 up 1 left ; and: cut a
    moves |= pos_rgt_cut_1 & (pos >> 17)        # shift:  2 up 1 right; and: cut h
    moves |= pos_rgt_cut_2 & (pos >> 10)        # shift:  1 up 2 right; and: cut g h

    return moves & 0xffffffffffffffff
