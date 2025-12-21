# download_verdict.py
import ssl
import certifi
import urllib.request
from pathlib import Path
import re

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
print("Total number of character:",len(raw_data))
print(raw_data[:99])
# Save to disk
file_path.write_bytes(raw_data)
print(f"Saved to {file_path.resolve()}")

# Decode bytes → string
text = raw_data.decode("utf-8")

# Tokenize: words and punctuation separate; collapse whitespace
pattern = r'([,.:;?_!"()\']|--|\s+)'   # capture punctuation & whitespace
tokens = re.split(pattern, text)
preprocessed = [t for t in tokens if t and not t.isspace()]

print(preprocessed[:30])
all_words = sorted(set(preprocessed))
vocab = len(all_words)
print(vocab)
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
