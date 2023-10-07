import sys
VOWEL = ['a', 'e', 'i', 'o', 'u']
for line in sys.stdin:
    if line.split() == ["#"]:
        break
    line = line.lower()
    count = 0
    for char in line:
        if char in VOWEL:
            count += 1
    print(count)