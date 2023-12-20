from pathlib import Path

# path = Path("pi_digits.txt")
path = Path("pi_million_digits.txt")
contents = path.read_text()
# contents = contents.rstrip()
# print(contents)
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
