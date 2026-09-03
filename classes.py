class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

emp1 = employee("swap", 24)
emp2 = employee("king", 12)

emp1.display()
emp2.display()