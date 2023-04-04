from generator import generator

print("\n(no_opt)" + 77 * "-" + "\n")

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)

# Le
# Lorem
# Ipsum
# est
# simplement
# du
# faux
# texte.

print("\n(ordered)" + 77 * "-" + "\n")

for word in generator(text, sep=" ", option="ordered"):
    print(word)

# Ipsum
# Le
# Lorem
# du
# est
# faux
# simplement
# texte.

print("\n(unique)" + 77 * "-" + "\n")

text = "Lorem Ipsum Lorem Ipsum hi La Lo la La Hi hi"
for word in generator(text, sep=" ", option="unique"):
    print(word)

# Lo
# la
# Hi
# hi
# Lorem
# La
# Ipsum

print("\n(bad arg)" + 77 * "-" + "\n")

for word in generator(text, sep=2):
    print(word)
for word in generator(text, sep=" ", option=42):
    print(word)
text = 1.0
for word in generator(text, sep="."):
    print(word)

# ERROR

print("\n(shuffle)" + 77 * "-" + "\n")

text = "Le Lorem Ipsum est simplement du faux texte. ah ah ah"
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("\n(dif sep)" + 77 * "-" + "\n")

text = "Le Lorem?Ipsum est ?simplement du faux !texte. ah? ah /ah"
for word in generator(text, sep="?"):
    print(word)

print()

for word in generator(text, sep="simplement"):
    print(word)

print()

text = "Le Lorem?Ipsum est \x03 simplement du faux !texte. ah? ah /ah"
for word in generator(text):
    print(word)

