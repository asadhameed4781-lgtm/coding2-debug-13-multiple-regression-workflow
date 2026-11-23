"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "2cc1f217e31ef23e1eaf76d1b0bef008"
GRADE_HASH = "2a8b75f1e4155debf9721a0100c45e05baa788b8afb6ca7f4cfc4680c74354ff"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
