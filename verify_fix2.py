import pickle
import json
import os
from target2_fixed import load_user_preferences as fixed_version

print("=== Testing the FIXED version ===\n")

if os.path.exists("proof2.txt"):
    os.remove("proof2.txt")

class MaliciousPayload:
    def __reduce__(self):
        return (os.system, ('echo hacked > proof2.txt',))

print("Trying the SAME malicious pickle payload from before...")
malicious_data = pickle.dumps(MaliciousPayload())

try:
    fixed_version(malicious_data)
except Exception as e:
    print(f"  --> The fixed function safely rejected it: {type(e).__name__}: {e}")

if os.path.exists("proof2.txt"):
    print("  --> FAILED: exploit still works!")
    exploit_blocked = False
else:
    print("  --> PASSED: exploit blocked, no file was created.")
    exploit_blocked = True

print("\nTrying normal, legitimate preferences (real JSON data this time)...")
legit_data = json.dumps({"theme": "dark", "language": "en"}).encode('utf-8')
result = fixed_version(legit_data)
print(f"  --> Result: {result}")
normal_input_works = (result == {"theme": "dark", "language": "en"})

print("\n=== VERDICT ===")
if exploit_blocked and normal_input_works:
    print("VERIFIED: the fix blocks the attack AND legitimate use still works.")
else:
    print("NOT VERIFIED: something's still off.")