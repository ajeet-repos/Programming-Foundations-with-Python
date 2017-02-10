import os

def rename_files():
    # 1. get file names from a folder
    file_list = os.listdir(r'C:\Users\dev\Google Drive\udacity\Programming Foundations with Python\prank')
    print(file_list)
    os.chdir('{}\prank'.format(os.getcwd()))
    # 2. rename the files without the numbers
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '0123456789'))


rename_files()