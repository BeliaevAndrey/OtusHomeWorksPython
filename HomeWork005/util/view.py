def field_print(mask: int) -> None:
    board = list(f'{mask:0>64b}')

    out = '\n'.join([''.join(f'{"X" if int(board[j * 8 + i]) else ".":^3}'
                             for i in range(8)) for j in range(8)])

    print(out, f'\n{len(board)}\n{"=" * 24}\n')
