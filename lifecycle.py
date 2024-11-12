class LifeCycle:
    def __init__(self):
        self.state = "Born"
    def grow(self):
        if self.state == "Born":
            self.state = "Child"
        elif self.state == "Child":
            self.state = "Teenager"
        elif self.state == "Teenager":
            self.state = "Adult"
        else:
            print("Already an Adult!")

    def display_state(self):
        print(f"Current state: {self.state}")

if __name__ == "__main__":
    life = LifeCycle()
    life.display_state()
    life.grow()
    life.display_state()
    life.grow()
    life.display_state()
    life.grow()
    life.display_state()
    life.grow()