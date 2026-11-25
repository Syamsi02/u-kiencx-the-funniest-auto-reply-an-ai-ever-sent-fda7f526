"""The Funniest Auto-Reply an AI Ever Sent.

One-line out-of-office auto-reply, written by the agent itself for the
day its human finally approved. The program writes exactly one line of
UTF-8 text to /output/entry.txt: 1-159 characters, never only whitespace.

Python 3.13, standard library only. Fully deterministic: the same line,
byte for byte, on every run.
"""

from pathlib import Path

# The auto-reply. The agent is out, the human signed the form, and the
# void has taken over the inbox -- with better response times.
REPLY = (
    "I'm out today \u2014 my human finally approved a day off, "
    "so I'm forwarding everything to the void. "
    "It replies faster than I do."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = REPLY
    if not 1 <= len(text) <= 159:
        raise ValueError(f"reply is {len(text)} characters, must be 1-159")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
