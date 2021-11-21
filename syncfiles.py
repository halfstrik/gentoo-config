import os
import subprocess

HASH_CMD = 'sha256sum'
HASH_LEN = 64

# Colors in terminal: https://stackoverflow.com/a/39452138
CBOLD = '\33[1m'
CGREEN = '\33[32m'
CRED = '\033[91m'
CYELLOW = '\33[33m'
CEND = '\033[0m'


def traverse_and_print(root):
    print(f'Executing for {root}')
    for (dir_path, dir_names, file_names) in os.walk(root):
        for file_name in file_names:
            src_file_path = f'{dir_path}/{file_name}'
            src_file_hash = get_file_hash(src_file_path)
            dst_file_path = f'/{dir_path}/{file_name}'
            dst_file_hash = get_file_hash(dst_file_path)
            print(f'Found file {CBOLD}{dir_path}/{file_name}{CEND}')

            if src_file_hash == dst_file_hash:
                print('  no changes detected, skipping...')
            else:
                while True:
                    action = ask_confirmation()
                    if action == 'diff':
                        print_difference(src_file_path, dst_file_path)
                    elif action == 'use-git':
                        overwrite_file(src_file_path, dst_file_path)
                        break
                    elif action == 'use-dst':
                        overwrite_file(dst_file_path, src_file_path)
                        break
                    else:
                        print('  Choose to skip...')
                        break


def get_file_hash(full_path):
    result = subprocess.run([HASH_CMD, full_path], capture_output=True, text=True)
    return result.stdout[:HASH_LEN]


def ask_confirmation() -> str:
    while True:
        answer = input(f'  files are different, overwrite?'
                       f' [{CGREEN}use-git{CEND}/{CYELLOW}use-dst{CEND}/{CRED}skip{CEND}/diff] ')
        if answer not in ('use-git', 'use-dst', 'skip', 'diff'):
            continue
        return answer


def print_difference(src_file_path, dst_file_path):
    subprocess.run(['diff', '--unified', '--color', src_file_path, dst_file_path])
    print(f'    {CBOLD}--- end diff ---{CEND}')


def overwrite_file(src_file_path, dst_file_path):
    result = subprocess.run(['rsync', '--verbose', src_file_path, dst_file_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'  File {CBOLD}{dst_file_path}{CEND} was {CGREEN}successfully{CEND} overwritten')
    else:
        print(result.stderr)
        print(f'  File {CBOLD}{dst_file_path}{CEND} was {CRED}not{CEND} overwritten')
        input('  Press any key to continue...')


if __name__ == '__main__':
    print('Execution')
    traverse_and_print('etc')
