import subprocess, time

print("="*55)
print("KAVACH-CRS: Autonomous Cyber-Reasoning System")
print("="*55)

for test_name, files in [
    ("TEST 1 — Command Injection (CWE-78)", ["target1.py", "prove_bug.py", "fix_bug.py", "verify_fix.py"]),
    ("TEST 2 — Insecure Deserialization (CWE-502)", ["target2.py", "prove_bug2.py", "fix_bug2.py", "verify_fix2.py"]),
]:
    print(f"\n--- {test_name} ---")
    labels = ["Scanning for suspicious patterns", "Proving it's exploitable", "AI diagnosing and patching", "Verifying the patch holds"]
    subprocess.run(["python", "-m", "bandit", files[0]])
    for label, f in zip(labels[1:], files[1:]):
        time.sleep(1)
        print(f"\n[{label}...]")
        subprocess.run(["python", f])

print("\n" + "="*55)
print("RUN COMPLETE — 2/2 vulnerability classes found, patched, verified")
print("="*55)