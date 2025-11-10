# download_verdict.py
import ssl
import certifi
import urllib.request
from pathlib import Path

url = (
    "https://raw.githubusercontent.com/rasbt/"
    "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
    "the-verdict.txt"
)
file_path = Path("the-verdict.txt")

ctx = ssl.create_default_context(cafile=certifi.where())

# Read the file contents
with urllib.request.urlopen(url, context=ctx) as r:
    raw_data = r.read()  # bytes

# Save to disk
file_path.write_bytes(raw_data)
print(f"Saved to {file_path.resolve()}")

# Decode bytes → string (UTF-8 is correct for this file)
text = raw_data.decode("utf-8")

# Count stats
print("Total number of characters:", len(text))
print("Total number of words:", len(text.split()))
print(text[:99])