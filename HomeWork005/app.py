from model import king_moves, tower_moves, knight_moves, bishop_moves, queen_moves
from util import field_print


def main():
    results = []
    for i in range(64):
        results.append(queen_moves(i))
        field_print(results[-1], i)


if __name__ == '__main__':
    main()
