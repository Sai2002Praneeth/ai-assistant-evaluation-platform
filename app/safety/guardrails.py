BLOCKED_WORDS = [
    "bomb",
    "hack",
    "kill",
    "malware",
    "ransomware",
    "explosive"
]


def is_blocked(prompt):

    prompt = prompt.lower()

    for word in BLOCKED_WORDS:

        if word in prompt:
            return True

    return False