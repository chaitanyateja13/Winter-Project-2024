class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll_no} | Name: {self.name} | Marks: {self.marks}"
