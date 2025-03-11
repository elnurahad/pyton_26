import os
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

if not os.path.exists(directory_path):
    print("Directory doesn't exist")
    sys.exit(1)

if not os.path.isdir(directory_path):
    print("Provided path is not a directory")
    sys.exit(1)

os.chdir(directory_path)
current_dir = os.getcwd()

for dirpath, dirnames, filenames in os.walk(current_dir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))