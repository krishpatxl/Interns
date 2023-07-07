class ButterChicken:
    def __init__(self, name, age, DOB, sex) -> None:
        self.name = name
        self.age = age
        self.date_of_birth = DOB
        self.sex = sex
        
        
person1 = ButterChicken("Krish", "18", "Jan 24", "Male")
person2a = ButterChicken("Bob", "18", "Dec 24", "Male")

print(person1.name)
print(person2.date_of_birth)    
    