"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt.
"""
import os

LINE = "Toast level 9 requested. I am a toaster, not a crematorium."

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)

if __name__ == "__main__":
    main()
