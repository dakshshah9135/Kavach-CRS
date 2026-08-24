import requests

import os
API_KEY = os.environ.get("GROQ_API_KEY")

vulnerable_code = '''
def check_host_alive(hostname):
    """Checks if a host responds to ping."""
    command = f"ping -n 1 {hostname}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode == 0
'''

prompt = f"""
You are a secure coding expert reviewing a confirmed security vulnerability.

VULNERABLE CODE:
{vulnerable_code}

CONFIRMED EVIDENCE:
- Malicious input that triggered the bug: "google.com & echo hacked > proof.txt"
- What happened: this created a file called proof.txt, even though the function is only supposed to check if a host responds to ping

Your tasks:
1. Name the vulnerability type using its CWE number and name.
2. Explain in 2-3 plain-language sentences why this specific code allows the attack.
3. Rewrite the function with the vulnerability fixed. It must still work correctly for normal, legitimate inputs — only close the security gap.

Respond in EXACTLY this format, nothing extra before or after:

CWE: <number and name>
EXPLANATION: <your explanation>
FIXED_CODE:
```python
<the complete corrected function>
```
"""

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": prompt}]
}

response = requests.post(url, headers=headers, json=data)
print("Status code:", response.status_code)

if response.status_code == 200:
    result = response.json()
    print(result["choices"][0]["message"]["content"])
else:
    print("Error details:", response.text)