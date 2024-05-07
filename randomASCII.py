import random
import string

x = 5

randomText = ""
for i in range(x):
    randomText += random.choice(string.ascii_letters)

print(randomText)