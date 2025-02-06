import os

source_dir = '/home/frank/Projects/MulFS-CAP/datasets/nirscene1'  # Current directory
for root, dirs, files in os.walk(source_dir):
    print(f"Current directory: {root}")
    print(f"Sub - directories: {dirs}")
    print(f"Files: {files}")
    print("-" * 50)
