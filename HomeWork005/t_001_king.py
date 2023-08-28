import os


def printer(mask: int) -> None:
    board = list(f'{mask:0>64b}')
    out = '\n'.join([''.join(f'{"X" if int(board[j * 8 + i]) else ".":^3}' for i in range(8)) for j in range(8)])
    print(out, f'\n{len(board)}\n{"=" * 24}\n')


def move(pos: int) -> int:
    pa = pos & 0xfefefefefefefefe
    ph = pos & 0x7f7f7f7f7f7f7f7f
    
    moves = (
            (pa << 7) | (pos << 8) | (ph << 9) |
            (pa >> 1) |              (ph << 1) |
            (pa >> 9) | (pos >> 8) | (ph >> 7)
    )
    return moves & 0xffffffffffffffff


files_path = '/home/andrew/Documents/OTUS/Algorithms/005_20230816/0.BITS/1.Bitboard - Король'
file_list = [os.path.join(files_path, file) for file in os.listdir(files_path) if file.startswith('test.')]

aggregate = []

for file in file_list:
    if file.endswith('in'):
        p = 1
        # print(file, file.replace('in', 'out'))
        with open(file, 'r') as f_in:
            try:
                test_in = int(f_in.read())
            except Exception as exc:
                print(f'{exc}')
                continue
        with open(file.replace('in', 'out'), 'r') as f_in:
            tests_out = [*map(lambda line: int(line.strip()), f_in.readlines())]
            # print(tests_out)
        check = move(p << test_in)
        # print(test_in, p << test_in, r := move(p << test_in), r == tests_out[1])
        aggregate.append(check == tests_out[1])
        print(aggregate[-1])

print(f'{aggregate.count(True)=}, {aggregate.count(False)=}')
print(''.join(map(str, map(int, aggregate))))
