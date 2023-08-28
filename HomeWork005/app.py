from model import king_move
from util import field_print


def main():
    results = []
    for i in range(64):
        results.append(king_move(i))
        field_print(results[-1])


if __name__ == '__main__':
    main()
