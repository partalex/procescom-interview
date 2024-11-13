import re
from rules import re_prefix
from log import Log
from helper import args_or_default

# file_path = args_or_default("../logs/debug.log")
file_path = args_or_default("../logs/debug.small.log")
# file_path = args_or_default("../logs/debug.test.log")
# file_path = args_or_default("../logs/debug.large.log")

log = Log(
    # error_output="../logs/error.log"
)

import time

start = time.time()

buffer = ""
try:
    with open(file_path, "r") as f:
        for line in f:
            if re.match(re_prefix, line):
                if buffer:
                    log.new_log(buffer)
                buffer = line
            elif buffer:
                buffer += line
            else:
                raise IndexError("Invalid log forrmat.")
        if buffer:
            log.new_log(buffer)
except IndexError as ve:
    print(f"ValueError: {ve}")
    exit(1)
except FileNotFoundError as fnfe:
    print(f"FileNotFoundError: {fnfe}")
    exit(1)
except Exception as e:
    print(f"Exception: {e}")
    exit(1)
finally:
    print(f"Time taken: {time.time() - start}")
print(log)
