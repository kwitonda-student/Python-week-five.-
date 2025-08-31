# Defining animal classes
class Cow:
    def move(self):
        print("The cow is walking slowly ")

class Elephant:
    def move(self):
        print("The elephant is marching heavily ")

class Ostrich:
    def move(self):
        print("The ostrich is running fast ")


# Polymorphism in action
for animal in [Cow(), Elephant(), Ostrich()]:
    animal.move()
