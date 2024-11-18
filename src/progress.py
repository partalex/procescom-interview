import os
import re
import threading
import time
from rules import re_prefix
from log import Log
from helper import args_or_default

file_path = args_or_default("../logs/debug.large.log")

log = Log(
    # error_output="../logs/error.log"
)

def print_progress():
    while True:
        time.sleep(1)
        file_size = os.path.getsize(file_path)
        processed_size = log.posstion
        progress = (processed_size / file_size) * 100
        print(f"Processed: {progress:.2f}%")

progress_thread = threading.Thread(target=print_progress)
progress_thread.daemon = True
progress_thread.start()

start = time.time()

buffer = ""
try:
    with open(file_path, "r") as f:
        print(f"File size: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB")
        for line in f:
            if re.match(re_prefix, line):
                if buffer:
                    log.new_log(buffer)
                buffer = line
            elif buffer:
                buffer += line
            else:
                raise IndexError("Invalid log format.")
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