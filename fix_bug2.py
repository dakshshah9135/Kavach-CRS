import requests

import os
API_KEY = os.environ.get("GROQ_API_KEY")

vulnerable_code = '''
def load_user_preferences(data_bytes):
    """Loads a user's saved preferences from serialized data."""
    preferences = pickle.loads(data_bytes)
    return preferences
'''

prompt = f"""
You are a secure coding expert reviewing a confirmed security vulnerability.

VULNERABLE CODE:
{vulnerable_code}

CONFIRMED EVIDENCE:
- Malicious input: a crafted pickle payload whose __reduce__ method calls os.system with a hidden command
- What happened: simply calling load_user_preferences() on this data executed the hidden command, creating a file the function was never told to create

Your tasks:
1. Name the vulnerability type using its CWE number and name.
2. Explain in 2-3 plain-language sentences why this specific code allows the attack.
3. Rewrite the function with the vulnerability fixed. It should still accept legitimate user preferences (a dictionary of settings) but must not use pickle.loads on untrusted data. Include any new import statement needed.

Respond in EXACTLY this format, nothing extra before or after:

CWE: <number and name>
EXPLANATION: <your explanation>
FIXED_CODE:
```python
<the complete corrected function, including any needed import>
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