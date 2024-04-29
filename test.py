def upperEverything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

loudRandomList: list[str] = upperEverything(["Ahmet", "Furkan", "Karatas"])

print(loudRandomList)