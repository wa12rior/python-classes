"""
Module that reads file structure
"""
import os


def print_dir(path=os.getcwd(), tabs=''):
    """
    Show directories structure recursively by provided path.

    :param tabs:
      Tabs in print to indent
    :param path:
      Directory path string. Default: current directory.
    """
    if tabs == '':
        if os.path.isfile(path):
            print('Podales nazwe pliku jako parametr')
            return False
        if path.split('\\')[-1] == '':
            print(path.split('\\')[-2], end='/\n')
        else:
            print(path.split('\\')[-1], end='/\n')
        tabs += '\t'

    for file in os.listdir(path):
        full_path = path + '\\' + file
        if os.path.isdir(full_path):
            print(tabs + file, end="/\n")
            os.chdir(full_path)
            print_dir(os.getcwd(), tabs=tabs + '\t')
        else:
            print(tabs + file)


if __name__ == '__main__':
    print_dir('C:\\Test')
