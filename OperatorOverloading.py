class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s= m1+m2
        return s

    def __str__(self):
        return f"Marks 1: {self.m1}, Marks 2: {self.m2}"

s1 = Student(45, 50)
s2 = Student(45, 50)

if __name__ == "__main__":
    s3 = s1 + s2
    print(s3)
