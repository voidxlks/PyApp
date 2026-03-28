# main.py

class App:
    def __init__(self):
        self.running = True

    def start(self):
        self.clear()
        print("Py App Started\n")

        while self.running:
            self.show_menu()

    def show_menu(self):
        print("Main Menu")
        print("1. Play Game")
        print("2. Settings")
        print("3. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            self.play_game()
        elif choice == "2":
            self.settings()
        elif choice == "3":
            self.exit_app()
        else:
            print("Invalid choice\n")

    def play_game(self):
        print("\nGame Starting...\n")

        # Example simple game (number guess)
        import random
        number = random.randint(1, 10)

        while True:
            guess = input("Guess a number (1-10) or 'q' to quit: ")

            if guess.lower() == "q":
                print("Exiting game...\n")
                break

            if not guess.isdigit():
                print("Enter a valid number")
                continue

            guess = int(guess)

            if guess == number:
                print("Correct!\n")
                break
            else:
                print("Wrong, try again")

    def settings(self):
        print("\nSettings")
        print("Nothing here yet\n")

    def exit_app(self):
        print("\nClosing app...")
        self.running = False

    def clear(self):
        import os
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    app = App()
    app.start()
