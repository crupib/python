#!/usr/bin/env python3

from pathlib import Path
from PIL import Image

TARGET_SIZE = (42, 42)

def resize_and_pad(file_path):
    try:
        with Image.open(file_path) as img:
            img = img.convert("RGBA")

            # Maintain aspect ratio
            img.thumbnail(TARGET_SIZE, Image.LANCZOS)

            # Create transparent canvas
            canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

            x = (TARGET_SIZE[0] - img.width) // 2
            y = (TARGET_SIZE[1] - img.height) // 2

            canvas.paste(img, (x, y), img)

            # Overwrite original
            canvas.save(file_path)

            print(f"Updated: {file_path}")

    except Exception as e:
        print(f"Failed: {file_path} -> {e}")


def main():
    root = Path.cwd()

    png_files = list(root.rglob("*.png"))

    if not png_files:
        print("No PNG files found.")
        return

    print(f"Found {len(png_files)} PNG files\n")

    for png_file in png_files:
        resize_and_pad(png_file)

    print("\nDone.")


if __name__ == "__main__":
    main()
