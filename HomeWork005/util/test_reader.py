import os

FILES_PATH = os.path.abspath('test_data/0.BITS')


def read_test(test_num: int = 1) -> dict[int, list[int, int]]:
    sub_dirs = sorted(os.listdir(os.path.abspath(FILES_PATH)))
    test_path = os.path.join(FILES_PATH, sub_dirs[test_num - 1])
    file_list = [os.path.join(test_path, file) for file in sorted(os.listdir(test_path)) if file.endswith('.in')]
    test_dct = {}
    for file in file_list:
        if file.endswith('in'):
            with open(file, 'r', encoding='utf-8') as f_in:
                with open(file.replace('in', 'out'), 'r', encoding='utf-8') as f_out:
                    try:
                        test_dct[int(f_in.read())] = [*map(lambda line: int(line.strip()), f_out.readlines())]
                    except Exception as exc:
                        print(f'{exc}')
                        continue
    return test_dct
