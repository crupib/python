from pathlib import Path
from PIL import Image

folder = Path(r".")

count = 0

for png_file in folder.rglob("*.png"):
    with Image.open(png_file) as img:
        print(
            f"Converting: {png_file.relative_to(folder)} "
            f"({img.width}x{img.height} -> 42x42)"
        )

        resized = img.resize((42, 42), Image.LANCZOS)
        resized.save(png_file)

    count += 1

print(f"\nDone. Converted {count} PNG file(s).")
