# app.py

class App:
    def __init__(self):
        self.running = True

    def start(self):
        print("Starting PyApp...\n")
        while self.running:
            self.menu()

    def menu(self):
        print("Main Menu")
        print("1. Hello")
        print("2. Simple Game")
        print("3. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            self.hello()
        elif choice == "2":
            self.game()
        elif choice == "3":
            self.exit()
        else:
            print("Invalid choice\n")

    def hello(self):
        name = input("Enter your name: ")
        print(f"Hello, {name}\n")

    def game(self):
        import random
        number = random.randint(1, 5)

        while True:
            guess = input("Guess a number (1-5) or 'q' to quit: ")

            if guess.lower() == "q":
                print("Exiting game...\n")
                break

            if not guess.isdigit():
                print("Enter a valid number")
                continue

            if int(guess) == number:
                print("Correct\n")
                break
            else:
                print("Wrong, try again")

    def exit(self):
        print("Closing app...")
        self.running = False


if __name__ == "__main__":
    app = App()
    app.start()
