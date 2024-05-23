exec('print("Hello World!")')

text: str = "print('Hola')"

loop: str = """
for i in range(3):
    print(i)
"""

exec(text)
exec (loop)

userInput: str = input("Write me a code: ")

exec(userInput)