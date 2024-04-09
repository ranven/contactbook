from tkinter import ttk, constants


class ContactsView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        # todo: handle logout view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._label = ttk.Label(
            master=self._frame,
            text="Contacts",
        )

        self._label.grid(padx=5, pady=5)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
