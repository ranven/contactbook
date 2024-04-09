from tkinter import Tk
from ui.ui import UI
from initialize_db import initialize_database


def main():
    initialize_database()

    window = Tk()
    window.title("Contact Book")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
