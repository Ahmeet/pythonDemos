import atexit

@atexit.register
def exitHandler() -> None:
    print("We are exiting now!")

@atexit.register
def goingToBeRemoved() -> None:
    print("You will not see tihs because i will unregister it!")

def main() -> None:
    for i in range(10):
        print(i)

if __name__ == "__main__":
    main()
    atexit.unregister(goingToBeRemoved)

# it can be really helpfull while closing db connections.
# or before closing commiting the changes
# closing files
# This decorator can handle it.
# even program raises an error this decorator will work anyway.
# we can unregister it to remove from the atexit.register stack.



