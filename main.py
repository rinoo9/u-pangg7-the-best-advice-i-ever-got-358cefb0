"""The Best Advice I Ever Got — one sentence, written to /output/entry.txt.

The line recalls a real moment: my grandmother stirring soup that had
simmered all day, and the sentence of hers I still taste whenever I am
tempted to hurry something that needs time.
"""

import os

LINE = "My grandmother, stirring soup that had simmered all day, said, \"Good things can't be rushed — neither can good people,\" and I still taste that patience whenever I want to hurry."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE, "line must be a single sentence with no newline"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
