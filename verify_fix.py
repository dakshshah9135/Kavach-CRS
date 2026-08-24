import os
from target1_fixed import check_host_alive as fixed_version

print("=== Testing the FIXED version ===\n")

if os.path.exists("proof.txt"):
    os.remove("proof.txt")

malicious_input = "google.com & echo hacked > proof.txt"
print(f"Trying the same malicious input: {malicious_input}")
fixed_version(malicious_input)

if os.path.exists("proof.txt"):
    print("  --> FAILED: exploit still works!")
    exploit_blocked = False
else:
    print("  --> PASSED: exploit blocked, no file was created.")
    exploit_blocked = True

print("\nTrying a normal, legitimate input: 127.0.0.1")
result = fixed_version("127.0.0.1")
print(f"  --> Result: {result}")
normal_input_works = (result == True)

print("\n=== VERDICT ===")
if exploit_blocked and normal_input_works:
    print("VERIFIED: the fix blocks the attack AND normal use still works.")
else:
    print("NOT VERIFIED: something's still off.")
