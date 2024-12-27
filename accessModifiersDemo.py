class MyClass:
    def __init__(self):
        self.publicVariable = 10
        self._privateVariable = 20
        self.__hiddenVariable = 30

    def printAll(self):
        print(self.publicVariable) # part of the public API
        print(self._privateVariable) # can still be accessed but not part of public API
        print(self.__hiddenVariable) # name mangling

    def publicMethod(self):
        print("Public Method")
    
    def _privateMethod(self):
        print("Private Method")

    def __hiddenMethod(self):
        print("Hidden Method")

myclass = MyClass()
myclass.printAll()

print(myclass.publicVariable)
print(myclass._privateVariable)
# print(myclass.__hiddenVariable)
print(myclass._MyClass__hiddenVariable)

myclass.publicMethod()
myclass._privateMethod()
# myclass.__hiddenMethod()
myclass._MyClass__hiddenMethod()