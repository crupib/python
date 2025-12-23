import ssl
import certifi
import urllib.request
import re

class SimpleTokenizerV1:
    def __init__(self,vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])',r'\1',text)
        return text

def download_file(url: str, file_path: str) -> None:
    # Create an SSL context that uses certifi's CA bundle
    ctx = ssl.create_default_context(cafile=certifi.where())

    # Download securely
    req = urllib.request.Request(url, headers={"User-Agent": "Python urllib"})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        data = resp.read()

    # Write to disk
    with open(file_path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    url = (
        "https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt"
    )
    file_path = "the-verdict.txt"

    download_file(url, file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    print(len(preprocessed))
    print(preprocessed[:30])
    all_words = sorted(set(preprocessed))
    vocab_size = len(all_words)
    print(vocab_size)
    vocab = {token:integer for integer, token in enumerate(all_words)}
    for i, item in enumerate(vocab.items()):
        print(item)
        if i >= 50:
            break
    print("********************* Using Class  ******************************")
    tokenizer = SimpleTokenizerV1(vocab)
    text = """"It's the last he painted, you know,"
           Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(text)
    print(ids)
    print(tokenizer.decode(ids))
    #mytext = "Hello, do you like tea?"
    #print(tokenizer.encode(mytext))
    all_tokens = sorted(list(set(preprocessed)))
    all_tokens.extend(["<|endoftext|>","<|unk|>"])
    vocab = {token:integer for integer, token in enumerate(all_tokens)}
    print(len(vocab.items()))
    for i, item in enumerate(list(vocab.items())[-5:]):
        print(item)
    for i, (key, value) in enumerate(list(vocab.items())):
        if key == "<|unk|>":
            print(f"found unk at index {i}: {key} -> {value}")
            break



