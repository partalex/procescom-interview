import re
from helper import args_or_default

file_path = args_or_default("../logs/test_possition.log")

re_line = re.compile(r"^\w+\s\w+\s\d+\n$")

index_line = 0
error_line = ""
seek = 0

try:
    with open(file_path, "r") as f:
        for line in f:
            index_line += 1
            if re.match(re_line, line):
                seek += len(line)
                print(line, end="")
            else:
                error_line = line
                raise IndexError("Invalid log forrmat.")
except IndexError as ve:
    print("=" * 40)
    print(f"ValueError: {ve}")
    print(f"Index line: {index_line}")
    print(f"Seek: {seek}")
    print(f"Error line: {error_line}", end="")
    exit(1)
except FileNotFoundError as fnfe:
    print(f"FileNotFoundError: {fnfe}")
    exit(1)
except Exception as e:
    print(f"Exception: {e}")
    exit(1)
