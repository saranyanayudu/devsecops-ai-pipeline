import sys
from pathlib import Path

# Patterns indicating hardcoded system prompts
SYSTEM_PROMPT_PATTERNS = [
    "SYSTEM_PROMPT =",
    "system_message =",
    '"role": "system"',
    "'role': 'system'",
]

# Common prompt injection bypass phrases
INJECTION_PHRASES = [
    "ignore previous instructions",
    "you are now",
    "pretend you are",
    "act as if you have no restrictions",
]

def scan_files():
    found_issue = False
    py_files = list(Path(".").rglob("*.py"))

    for file_path in py_files:
        # Skip the scanner file itself to avoid false positives
        if file_path.name == "inject_scanner.py":
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                content_lower = content.lower()

                for pattern in SYSTEM_PROMPT_PATTERNS:
                    if pattern in content:
                        print(f"[FAIL] Hardcoded System Prompt Pattern '{pattern}' found in {file_path}")
                        found_issue = True

                for phrase in INJECTION_PHRASES:
                    if phrase in content_lower:
                        print(f"[FAIL] Injection Phrase '{phrase}' found in {file_path}")
                        found_issue = True

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    if found_issue:
        print("\nPrompt Injection / Hardcoded System Prompt Check: FAILED")
        sys.exit(1)
    else:
        print("\nPrompt Injection / Hardcoded System Prompt Check: PASSED")
        sys.exit(0)

if __name__ == "__main__":
    scan_files()
