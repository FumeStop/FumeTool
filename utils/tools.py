from __future__ import annotations

from typing import Union

import re
import random

_faces = [
    "(*^ω^)",
    "(*^.^*)",
    "owo",
    "OwO",
    "uwu",
    "UwU",
    "(*￣>￣)",
    ">w<",
    "^w^",
    "(/ =w=)/",
]

_patterns = {
    r"[lr]": "w",
    r"[LR]": "W",
    r"n([aeiou])": "ny\\1",
    r"N([aeiou])": "Ny\\1",
    r"N([AEIOU])": "NY\\1",
    "th": "d",
    "ove": "uv",
    "no": "nu",
}


def parse_cooldown(retry_after: Union[int, float]) -> tuple[int, int]:
    retry_after = int(retry_after)

    hours, remainder = divmod(retry_after, 3600)
    minutes, seconds = divmod(remainder, 60)

    return minutes, seconds


def owo_fy(text: str) -> str:
    for pattern, repl in _patterns.items():
        text = re.sub(pattern, repl, text)

    return random.choice(_faces) + "\n" + f"```css\n{text}\n```"


def format_boolean_text(text: Union[str, bool]) -> str:
    if isinstance(text, bool):
        return "Yes" if text else "No"

    return text.replace("True", "Yes").replace("False", "No")
