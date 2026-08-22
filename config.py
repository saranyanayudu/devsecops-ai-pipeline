# Hardcoded API key (deliberate fail)
# Hardcoded secret pattern for Gitleaks
import os

# Fetch secret safely from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-proj-1234567890abcdef1234567890abcdef")
