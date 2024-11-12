class SampleClass:
    def __init__(self, name):
        self.name = name
    def display_message(self):
        print(f"Hello, {self.name}! Welcome to the Sample Class.")

if __name__ == "__main__":
    obj = SampleClass("User")
    obj.display_message()