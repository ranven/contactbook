from tkinter import Tk
from ui.main import UI


def main():
    window = Tk()
    window.title("Contact Book")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
