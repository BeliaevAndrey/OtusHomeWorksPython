def field_print(mask: int, pos: int = None) -> None:
    board = [*map(int, f'{mask:0>64b}')]
    if pos is not None:
        board[63 - pos] = 3
    else:
        pos = ''
    out = '\n'.join([''.join(f'{"X" if board[j * 8 + i] == 1 else "F" if board[j * 8 + i] == 3 else ".":^3}'
                             for i in range(7, -1, -1)) for j in range(8)])

    print(pos, '\n', out, f'\n{"=" * 24}\n', sep='')
