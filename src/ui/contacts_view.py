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
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        top_frame = ttk.Frame(master=self._frame)
        top_frame.pack(fill=constants.X)

        logout_button = ttk.Button(
            master=top_frame,
            text="Log out",
            command=self._logout_handler
        )
        logout_button.pack(side=constants.RIGHT, padx=5, pady=5)

        create_button = ttk.Button(
            master=top_frame,
            text="Create new",
            command=self._handle_create
        )
        create_button.pack(side=constants.RIGHT, padx=5, pady=5)

        header_label = ttk.Label(
            master=self._frame,
            text="Contacts",
            font=("Helvetica", 16)
        )
        header_label.pack(pady=10)

        self._contacts = contact_service.get_contacts()

        for contact in self._contacts:
            self._initialize_contact(contact)

    def _initialize_contact(self, contact):
        style = ttk.Style()
        style.configure("ContactFrame.TFrame", background="white")
        style.configure("ContactLabel.TLabel", background="white")

        contact_frame = ttk.Frame(
            master=self._frame, style="ContactFrame.TFrame")
        contact_frame.config(padding=8, borderwidth=1)

        first_name_label = ttk.Label(
            master=contact_frame, text="First Name:", style="ContactLabel.TLabel")
        first_name_label.grid(row=0, column=0, sticky="w")

        first_name_value = ttk.Label(
            master=contact_frame, text=contact.first_name, style="ContactLabel.TLabel")
        first_name_value.grid(row=0, column=1, sticky="w")

        last_name_label = ttk.Label(
            master=contact_frame, text="Last Name:", style="ContactLabel.TLabel")
        last_name_label.grid(row=1, column=0, sticky="w")

        last_name_value = ttk.Label(
            master=contact_frame, text=contact.last_name, style="ContactLabel.TLabel")
        last_name_value.grid(row=1, column=1, sticky="w")

        email_label = ttk.Label(
            master=contact_frame, text="Email:", style="ContactLabel.TLabel")
        email_label.grid(row=2, column=0, sticky="w")

        email_value = ttk.Label(
            master=contact_frame, text=contact.email, style="ContactLabel.TLabel")
        email_value.grid(row=2, column=1, sticky="w")

        phone_label = ttk.Label(
            master=contact_frame, text="Phone:", style="ContactLabel.TLabel")
        phone_label.grid(row=3, column=0, sticky="w")

        phone_value = ttk.Label(
            master=contact_frame, text=contact.phone, style="ContactLabel.TLabel")
        phone_value.grid(row=3, column=1, sticky="w")

        contact_frame.pack(fill=constants.X, padx=10, pady=(5, 0))
