import os
import sys

if len(sys.argv) > 1:
    mb_size = int(sys.argv[1])
else:
    mb_size = 20
MB = 1024 * 1024
file_size_b = MB * mb_size

sample_start = "2024-08-25 23:05:14 | /api7/app/getActivePackages.php?appId=QP1A.190711.020-e082f2e0-e343-1051-9f58-7b8f8b4dc01e&userId=390026665&platform=GOOGLE&appName=globaltel_sc&lang=sr | Database query ok: SQL query: SELECT * FROM devices WHERE user_id='390026665' AND registered='TRUE' and app_name ='globaltel_sc' LIMIT 1 \n2024-08-25 23:05:14 | /api7/app/getActivePackages.php?appId=QP1A.190711.020-e082f2e0-e343-10 51-9f58-7b8f8b4dc01e&userId=390026665&platform=GOOGLE&appName=globaltel_sc&lang=sr | verifyDevice => app_hash from request:QP1A.190711.020-e082f2e0-e343-1051-9f58-7b8f8b4dc01e\n"

sample_error = "2024-08-25 23:05:20 | /api7/app/getAccountDetails.php?app_id=c4dfd41eb1503267-66ee21e0-cf11-11ee-8b02-b9b08d3f0f2d&user_id=385374190&platform=GOOGLE&appName=globaltel_sc | ERROR: Account balance retrieval failed\n"

sample_process = "2024-08-25 23:05:18 | /api7/app/getBalance.php?user_id=385374190&app_id=c4dfd41eb1503267-66ee21e0-cf11-11ee-8b02-b9b08d3f0f2d&platform=GOOGLE&appName=globaltel_sc | START PROCESS\n"

sample_log = (
    "2024-08-25 23:05:14 | /api7/app/getActivePackages.php?appId=QP1A.190711.020-e082f2e0-e343-1051-9f58-7b8f8b4dc01e&userId=390026665&platform=GOOGLE&appName=globaltel_sc&lang=sr | "
    "Database query ok: SQL query: SELECT * FROM devices WHERE user_id='390026665' AND registered='TRUE' and app_name ='globaltel_sc' LIMIT 1\n"
)

repetitions = file_size_b // len(sample_log)

import time

start = time.time()
try:
    info = {
        "Logs": 0,
        "Errors": 0,
    }
    with open('debug.large.log', 'w') as f:
        f.write(sample_start)
        info["Logs"] += 2
        for _ in range(repetitions):
            random_number = os.urandom(1)[0]
            if random_number % 100 < 5:
                f.write(sample_error)
                info["Errors"] += 1
            elif random_number % 100 < 10:
                f.write(sample_process)
            else:
                f.write(sample_log)
            info["Logs"] += 1

    print(f"Time taken: {time.time() - start}")
    for key, value in info.items():
        print(f"{key}: {value}")
    print(f"File size: {os.path.getsize('debug.large.log') / MB} MB")

except Exception as e:
    print(f"Error opening file: {e}")
    exit(1)
