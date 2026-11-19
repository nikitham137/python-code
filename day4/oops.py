class college:
    name="Goplan University"
    loc="Hoodi"
     
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept

    def display(self):
        print(self.name, self.age, self.dept)
        