from model import king_moves, count_pop, knight_moves, tower_moves, bishop_moves, queen_moves
from util import read_test

FORMAT = 'position: {0:<5} check moves amt: {1:<6}; check moves: {2:<6}'


def test_king_moves():
    test_dct = read_test()
    for i_key, i_val in test_dct.items():
        mask = king_moves(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def test_knight_moves():
    test_dct = read_test(2)
    for i_key, i_val in test_dct.items():
        mask = knight_moves(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def test_tower_moves():
    test_dct = read_test(3)
    for i_key, i_val in test_dct.items():
        mask = tower_moves(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def test_bishop_moves():
    test_dct = read_test(4)
    for i_key, i_val in test_dct.items():
        mask = bishop_moves(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def test_queen_moves():
    test_dct = read_test(5)
    for i_key, i_val in test_dct.items():
        mask = queen_moves(i_key)
        moves_amt = count_pop(mask)
        print(FORMAT.format(i_key, str(moves_amt == i_val[0]), str(mask == i_val[1])))


def main():
    print(f'\n{" King ":=^80}\n')
    test_king_moves()
    print(f'\n{" Knight ":=^80}\n')
    test_knight_moves()
    print(f'\n{" Tower ":=^80}\n')
    test_tower_moves()
    print(f'\n{" Bishop ":=^80}\n')
    test_bishop_moves()
    print(f'\n{" Queen ":=^80}\n')
    test_queen_moves()


if __name__ == '__main__':
    main()
