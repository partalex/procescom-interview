import re

from rules import re_error, re_process


class Log:
    def __init__(self, error_output=""):
        self.total_logs = 0
        self.invalid_logs = 0
        self.max_length = 0
        self.max_log = ""
        self.posstion = 0
        self.process_stated = False
        self.logs_in_process = 0
        self.error_output = error_output
        if self.error_output:
            self.error_file = open(error_output, "w")

    def check_error(self, log):
        if re.search(re_error, log):
            self.invalid_logs += 1
            if self.error_output:
                self.error_file.write(log + "\n")

    def check_process(self, log):
        if re.search(re_process, log):
            self.process_stated = True
            self.logs_in_process = 0
        elif self.process_stated:
            self.logs_in_process += 1

    def __del__(self):
        if self.error_output:
            self.error_file.close()

    def new_log(self, log):
        log = log.strip()
        lenght = len(log)
        # self.posstion += lenght
        if lenght > self.max_length:
            self.max_length = lenght
            self.max_log = log
        self.check_error(log)
        self.check_process(log)
        self.total_logs += 1

    def __str__(self):
        return (f"Logs: {self.total_logs}"
                f"\nErrors: {self.invalid_logs}"
                f"\nLogs in process: {self.logs_in_process}"
                f"\nLongest log: {self.max_length}"
                f"\nLongest: {self.max_log}")