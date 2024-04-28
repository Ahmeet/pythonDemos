users: dict[int, str] = {0: "Bob", 1: "Mario"}

user: str | None = users.get(3)

if user:
    print(f"{user} exist!")
else:
    print("No user found...")


# with walrus operator
# first it well get evaluated then check with the if statement.

if user := users.get(3):
    print(f"{user} exist!")
else:
    print("No user found...")

############################################################

def getInfo(text: str) -> dict:
    return {"words": (words := text.split()),
            "wordCount": len(words),
            "characterCount": len("".join(words))} # we must use paranthesis to work with walrus inside this.

print(getInfo("Bob"))
print(getInfo("Hello Bob"))
print(getInfo("My name is not Bob!"))