class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Student name: ", self.name)
        print("Student age: ", self.age)

s1 = student("Pragya", 12)
s2 = student("Bhavya", 13)

s1.show_details()
print()
s2.show_details()
print()