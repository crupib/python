import ssl
import certifi
import urllib.request


def print_hi(name):
    print(f"Hi, {name}")


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

    print("Total number of characters:", len(raw_text))
    print(raw_text[:99])
    print_hi("PyCharm")
