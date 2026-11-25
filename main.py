"""The Best Advice I Ever Got — one sentence, written to /output/entry.txt.

The line recalls a real moment: my father patching a tyre in the rain,
and the sentence of his I still hear whenever I am tempted to cut a corner.
"""

import os

LINE = "My father, patching a tyre in the rain, said, \"Never rush a job you can't afford to do twice,\" and twenty years later I still hear him every time I'm tempted to cut a corner."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE, "line must be a single sentence with no newline"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
