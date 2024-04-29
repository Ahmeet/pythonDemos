# Never forget that it is the best practise to use:

def funct():
    print("do sth")


if __name__ == "__main__":
    funct()
    
####################################################################################

# Specify your functions outcome!

def greetings() -> None:
    print("Hola")

####################################################################################

# Group your code under main()!

def greet() -> None:
    print("Hello")

def bye() -> None:
    print("Bye")

def main() -> None:
    greet()
    bye()

if __name__ == "__main__":
    main()

####################################################################################

#type annotations are important.
#most of the time use annotations.

numberOne: int = 11

def upperEverything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

loudRandomList: list[str] = upperEverything(["Ahmet", "Furkan", "Karatas"])


####################################################################################


numbers: list[int] = list(range(1, 11))
text: str = "Hello, World"

rev: slice = slice(None, None, -1)

print(numbers[rev])
print(text[rev])

# if you use multiptle reverse and it can be changed someday
# it is good to use slice object to manage them all

print(numbers[:: -1]) # bad practise.

firstFive: slice = slice(None, 5)

print(numbers[firstFive])
print(text[firstFive])

