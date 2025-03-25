class Student:
    def __init__(self, name: str, marks: list = []):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        # założyłem, że chodziło o średnią 5.0
        return sum(self.marks) / len(self.marks) > 5.0

    def __str__(self):
        return (
            f"Student: {self.name}\nMarks: {self.marks}\nPassed: {self.is_passed()}\n"
        )
