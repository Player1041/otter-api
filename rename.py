import os
import re

folder_path = 'photos'  # Replace with the path to your folder
regex_pattern = r'(.*?)(\.\w+)?$'

files = os.listdir(folder_path)
files.sort()

for index, filename in enumerate(files):
    new_filename = f'{index + 1}{os.path.splitext(filename)[1]}'
    new_filepath = os.path.join(folder_path, new_filename)
    old_filepath = os.path.join(folder_path, filename)
    os.rename(old_filepath, new_filepath)