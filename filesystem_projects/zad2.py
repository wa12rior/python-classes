"""
Module responsible for sorting files and making class directories for them.
"""
import os
import shutil


def collect_files(path=os.getcwd()):
    """
    Gets all files in directory structure.

    :param path:
      Directory path.
    :return file_list:
      List with files in directory.
    """

    file_list = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        file_list += [os.path.join(dirpath, file) for file in filenames]
    return file_list


def create_categories(path, dirs):
    """
    Function creates directories for sorted files.

    :param path:
      Path to create categories.
    :param dirs:
      Dict with keys as directories' names
    """
    for directory_name in dirs.keys():
        os.makedirs(path + '\\' + directory_name, exist_ok=True)


def in_other_files(file, dirs):
    """
    Checks if file is in other files category

    :param file:
      Filename.
    :param file:
      Dict with directories and matching extensions.
    """
    for ext in dirs.values():
        if file.split('.')[-1] in ext:
            return False
    return True


def delete_empty_dirs(path, dirs):
    """
    Function deletes empty directories.

    :param path:
      Path to create categories.
    :param dirs:
      Dict with keys as directories' names
    """
    trash_dirs = [directory for directory in os.listdir(path) if directory not in dirs.keys()]
    for directory in trash_dirs:
        shutil.rmtree(path + '\\' + directory)


def sort_files(path, dirs):
    """
    Sorts files by extension and class.
    Creating directories for sorting and deleting unused dirs.

    :param path:
      Source path.
    :param dirs:
      Dict with directories and matching extensions.
    """
    files = collect_files(path)
    create_categories(path, dirs)

    other_files = [file for file in files if in_other_files(file, dirs)]
    ext_files = [item for item in files if item not in other_files]

    for file in ext_files:
        for category in dirs.items():
            if file.split('.')[-1] in category[1]:
                destination_path = path + '\\' + category[0]
                if file != destination_path + '\\' + file.split('\\')[-1]:
                    shutil.move(file, destination_path)

    for file in other_files:
        destination_path = path + '\\OTHER_FILES'
        if file != destination_path + '\\' + file.split('\\')[-1]:
            shutil.move(file, destination_path)

    delete_empty_dirs(path, dirs)


if __name__ == '__main__':
    PATH = 'C:\\Test\\test'
    CATEGORIES = {
        'DOCUMENTS': ['pdf', 'docx', 'xls'],
        'PICTURES': ['png', 'jpg', 'tff', 'bmp', 'gif'],
        'SOURCECODE': ['py', 'php', 'c'],
        'DRAFTS': ['txt'],
        'OTHER_FILES': []
    }

    sort_files(PATH, CATEGORIES)
