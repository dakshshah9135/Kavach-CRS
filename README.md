# Kavach-CRS
### An Autonomous Cyber-Reasoning System for Self-Healing Code

Built for AI Kavach, Terrier Cyber Quest 2026.

## The Problem
Scanners find vulnerabilities and stop. A human still has to interpret the finding, write a fix, test it, and confirm it worked — every unpatched gap in between is a live risk window.

Can a system find a real weakness, fix it, and prove the fix holds — with zero human intervention?

## How It Works
1. **Static Analysis** (Bandit) — flags a suspicious pattern.
2. **Exploit Proof** — a custom oracle-based check confirms the flaw is genuinely exploitable, not a guess.
3. **AI Diagnosis & Patch** — an LLM (Llama 3.3 70B via Groq) reasons only over confirmed evidence — never raw code alone — and drafts a fix.
4. **Verification** — the original exploit is re-run (must now fail); legitimate use is re-tested (must still pass).

## Verified Results
**Test 1 — Command Injection (CWE-78):** `target1.py` pings a host using `subprocess` with `shell=True`. Bandit flags it. A crafted input proved it exploitable. The AI rewrote the call as a safe argument list. Verified: exploit blocked, normal use intact.

**Test 2 — Insecure Deserialization (CWE-502):** `target2.py` loads data with `pickle.loads()`. Bandit flags it. A crafted payload proved that simply loading the data executes a hidden command. The AI recognized `pickle` was the wrong tool entirely and switched to `json`. Verified: exploit blocked, legitimate JSON still loads.

## Run It

pip install -r requirements.txt
$env:GROQ_API_KEY="your-key-here"
python run_kavach_crs.py


## Tech Stack
Python 3 · Bandit · Groq API (Llama 3.3 70B, free tier)

## Team
Daksh Shah · Param Shah · Heet Gohil — Shah & Anchor Kutchhi Engineering College