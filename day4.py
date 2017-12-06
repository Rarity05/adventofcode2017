input = open("inputs/day4.txt")
passphrases = []
for line in input:
    passphrases.append(line.split())

# part 1
passphrases = passphrases

# part 2
passphrases = list(map(lambda passphrase: list(map(lambda word: "".join(sorted(word)), passphrase)), passphrases))

valid = sum(map(lambda x: 1 if len(x) == len(set(x)) else 0, passphrases))
print("Result:", valid)
