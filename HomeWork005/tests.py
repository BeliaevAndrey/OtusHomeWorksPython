from model import king_move, count_pop
from util import read_test

FORMAT = 'position: {0:<5} check moves amt: {1:<6}; check moves: {2:<6}'


def test_king_moves():
    test_dct = read_test()
    for i_key, i_val in test_dct.items():
        mask = king_move(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def test_knight_moves():
    test_dct = read_test(2)
    for i_key, i_val in test_dct.items():
        mask = king_move(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def main():
    print(f'\n{" King ":=^80}\n')
    test_king_moves()
    print(f'\n{" Knight ":=^80}\n')
    test_knight_moves()


if __name__ == '__main__':
    main()
