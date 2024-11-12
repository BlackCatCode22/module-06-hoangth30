class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

if __name__ == "__main__":
    dog = Dog("Rex")
    cat = Cat("Whiskers")
    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")