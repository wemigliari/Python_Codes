# Translator

#vowels -> g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "ggg"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a word or phrase: ")))

#Or
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.upper():
                translation = translation + "GGG"
            else:
                translation = translation + "ggg"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a word or phrase starting with vowel: ")))