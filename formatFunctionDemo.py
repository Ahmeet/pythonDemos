class Book:
    def __init__(self, title: str, pagaes: int) -> None:
        self.title = title
        self.pages =pagaes
    
    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case "time":
                return f"{self.pages / 60:.2f}"
            case "caps":
                return f"{self.title.upper()}"
            case _:
               raise ValueError(f"Unknown specifier for Book()")

def main() -> None:
    hairyPotter: Book = Book("Very Hairy Potter", 300)
    pythonDaily: Book = Book("Python Daily", 20)

    print(f"{hairyPotter:caps}")

    print(f"Read time: {hairyPotter:time}")

if __name__ == "__main__":
    main()