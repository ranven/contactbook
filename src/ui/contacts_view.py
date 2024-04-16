from tkinter import ttk, constants
from services.user_service import user_service
from services.contact_service import contact_service


class ContactCreationError(Exception):
    pass


class ContactsView:
    def __init__(self, root, handle_logout, handle_create):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_create = handle_create
        self._contacts = []
        self._contact_form_frame = None
        self._contact_form_view = None
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

        create_button = ttk.Button(
            master=self._frame,
            text="Create new",
            command=self._handle_create
        )

        self._label.grid(padx=5, pady=5)
        logout_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        self.contacts = contact_service.get_contacts()

        for contact in self._contacts:
            self._initialize_contact(contact)

    def _initialize_contact(self, contact):
        contact_frame = ttk.Frame(master=self._frame)

        project_title = ttk.Label(
            master=contact_frame, text=contact.first_name)
        project_title.grid(row=1, column=0)

        contact_frame.config(padding=16, border=2)
        contact_frame.pack()
