from functools import partial

def specifications(colour: str, name: str, amount: int) -> None:
    print(f"Specs: {colour=}, {name=}, {amount=}")

specifications("Red", "Bob", 5)
specifications("Red", "Bob", 10)
specifications("Red", "Bob", 50)
# Only amount changes so we can do this.

specifyAmount:partial = partial(specifications, "Red", "Bob")
specifyAmount(5)
specifyAmount(10)
specifyAmount(50)


specifyColourAndName:partial = partial(specifications, amount=10) # Amount will be 10

specifyColourAndName("Red", "Bob")
specifyColourAndName("Yellow", "Green")


specifyName:partial = partial(specifications, "Green", amount=10_000)

specifyName("Ali")
specifyName("Veli")
specifyName("Ahmet")
specifyName("Mehmet")