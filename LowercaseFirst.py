phrase = ""
lowerPhrase = ""
upperPhrase = ""
newPhrase = ""

phrase = input("What do you have to say?: ")

for ch in phrase:
    if ch.isspace() == False:
        if ch.islower():
            lowerPhrase = lowerPhrase + ch
        if ch.isupper():
            upperPhrase = upperPhrase + ch

newPhrase = lowerPhrase + upperPhrase

print(newPhrase)