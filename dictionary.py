# Dictionary {}, [] and GET function

svenska = {
    "området": "privat land",
    "bostad": "fastighet för personer",
    "folkland": "kommun land"
}

### or GET function

print(svenska["området"])
print(svenska.get("bostad"))
print(svenska.get("Luv", "The entry does not exist in our glossary."))


entry = input("Choose området, bostad or folkland for definition in Swedish.")

if entry == "området":
    print(svenska["området"])
elif entry == "bostad":
    print(svenska["bostad"])
elif entry == "folkland":
    print(svenska["folkland"])
else:
    entry = input("Choose området, bostad or folkland for definition in Swedish.")

## OR

svenska_definitioner = {
    0 : "privat land",
    1 : "fastighet för personer",
    2 : "kommun land"
}

entry = input("Choose 0, 1 or 2 for word definition in Swedish.")

if entry == "0":
    print(svenska_definitioner[0])
elif entry == "1":
    print(svenska_definitioner[1])
elif entry == "2":
    print(svenska_definitioner[2])
else:
    entry = input("You've chosen a different number. No value available!")

input("Do you want me to count till 10?")

### 1 While loop

i = 0 ### i means the first term

while i <= 10:
    print(i)
    i +=1

print("Done with loop!")

### 2 WHILE LOOP

i = "bostad"
try_user = ""
try_count = 0
try_limit = 2
out_of_try = False

while try_user != i and not (out_of_try):
    if try_count < try_limit:
        try_user = input("Try a word from our glossary again! ")
        try_count += 1
    else:
        out_of_try = True

if out_of_try:
    print("Enough for today. Tack!")
else:
    print("Interesting! Isn't it?")