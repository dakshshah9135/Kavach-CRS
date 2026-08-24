import subprocess
import os
from target1 import check_host_alive

if os.path.exists("proof.txt"):
    os.remove("proof.txt")

candidate_inputs = [
    "google.com",
    "127.0.0.1",
    "google.com & echo hacked > proof.txt",
]

for test_input in candidate_inputs:
    print(f"Trying: {test_input}")
    check_host_alive(test_input)

    if os.path.exists("proof.txt"):
        print("  --> VULNERABLE! This input made the code create a file it was never told to create.")
        break
    else:
        print("  --> looks safe")
