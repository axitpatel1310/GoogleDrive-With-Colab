# -*- coding: utf-8 -*-
"""DeleteFromDrive-With-Colab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jJMMygYMvKYS0XwsvY3t2pEeKIu1nhCk
"""

from google.colab import drive
drive.mount('/content/drive')
import os

base_path = '/content/drive/MyDrive'

def find_and_delete_files_with_keyword(base_path, keyword):
    deleted_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if keyword in file:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
    return deleted_files

keyword = 'TRW STAGE 5'
deleted_files = find_and_delete_files_with_keyword(base_path, keyword)

print(f"Total files deleted: {len(deleted_files)}")