firstNumber: int = 1_000_000_000

secondNumber: int = 1,000,000,000

thirdNumber: int = 1000000000

print(f"{thirdNumber:_}")
print(f"{thirdNumber:,}")

print("#############################################################################")

var = "something"

print(f"{var:>20}") # it will consume 20 characther space but value will write the right hand side

print(f"{var:<20}") # it will consume 20 characther space but value will write the left hand side

#left one is the default so you can use this

print(f"{var:20}")

print(f"{var:^20}") # it will consume 20 characther space but value will write the center

# also we can fill it anything we want

print(f"{var:.^20}")
print(f"{var:i^20}")


print("#############################################################################")

from datetime import datetime
now = datetime.now()

print(f"{now:%d.%m.%y}")

print(f"{now:%H.%M.%S}")

print(f"{now:%c}")

print(f"{now:%I%p}")

# nest fString

dateTimeSpecifier: str = "%d.%m.%y"

print(f"{now:{dateTimeSpecifier}}")

# you can search it datetime format specifiers.


print("#############################################################################")

n: float = 1234.56789

print(round(n, 2))

print(f"{n:.2f}") # it is like round function

print(f"{n:,.2f}") # thousand seperator

print(f"{n:.0f}") # it will round an integer


print("#############################################################################")


a: int = 5

b: int = 10

myVar: str = "Hello"

print(f"a + b = {a + b}")

print(f"{a + b = }") # anything before the equal sign will maintained.

print(f"{bool(a) = }")

c: float = 0.1

d: float = 0.2

print(f"{c + d = :.1f}")

print(f"{myVar = }")

print(f"{myVar = !s}")


print("#############################################################################")

# Scientific Notation

bigNumber: int = 1_598_000_000

print(f"{bigNumber:e}")

print(f"{bigNumber:.2e}")


print("#############################################################################")


# path sometimes get tricky because \n \f \U make trouble.

customFolder: str = "Indently"

path: str = r"\Users\oakwood\Documents\Personal\folder" # it is a raw string

print(path)

customPath: str = fr"\Users\oakwood\Documents\Personal\{customFolder}"

print(customPath)


print("#############################################################################")


from datetime import date

banana: str = "🍌"

name: str = "Ahmet"

today: date = datetime.now().date()

print(f"[{today!s}] {name!s} says: {banana!s}") # normal

print(f"[{today!r}] {name!r} says: {banana!r}") # raw

print(f"[{today!a}] {name!a} says: {banana!a}") # ASCII