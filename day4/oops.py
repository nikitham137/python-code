class college:
    name = "Goplan University"
    loc = "Hoodi"
    
    @classmethod
    def disp(cls):
        print(cls.name,cls.loc)

    def __init__(self, name, age, dept, sub):
        self.name = name
        self.age = age
        self.dept = dept
        self.sub = sub

    def display(self):
        print(self.name, self.age, self.dept, self.sub)

    def change_name(self, new_name):
        self.name = new_name


s1 = college("Priya", 20, "AI", "Maths")
s2 = college("Ruby", 21, "ME", "CAD")
print("Before changing name")
s1.display()
s2.display()
s2.change_name("Gopi")
print("After changing name")
s2.display()
print("*********************")
college.change_name(s1, "Gopi")
s1.display()
s1.disp()
s2.disp()