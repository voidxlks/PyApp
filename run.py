# run.py

import sys


def main():
    try:
        from main import App
    except ImportError:
        print("Error: main.py not found or App class missing.")
        sys.exit(1)

    try:
        app = App()
        app.start()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
