sen =  input("Please provide a sentence. ")

alphabet = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0
}

for letter in sen:
    if letter in alphabet:
        alphabet[letter] +=1

print(alphabet)

pangram = True
for val in alphabet.values():
    if val == 0:
        pangram = False

if pangram:
    print("It is a pangram sentence, which means it has all the letters in the alphabet in one sentence.")
else:
    print("That is not a pangram, which means it does not have all the letter in the alphabet in one sentence")