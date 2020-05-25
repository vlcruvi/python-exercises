
phrase = ("I am an elite hacker")
hacker_phrase = ""

for c in phrase.lower():
    if c == "a":
        hacker_phrase += "4"
    elif c == "e":
        hacker_phrase = hacker_phrase + "3"
    elif c == "l":
        hacker_phrase = hacker_phrase + "1"
    elif c == "t":
        hacker_phrase = hacker_phrase + "t"
    else:
        hacker_phrase = hacker_phrase + c

print(hacker_phrase) 

        