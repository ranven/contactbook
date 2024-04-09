from tkinter import ttk, constants
from services.user_service import user_service


class ContactsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._label = ttk.Label(
            master=self._frame,
            text="Contacts",
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._logout_handler
        )

        self._label.grid(padx=5, pady=5)
        logout_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
