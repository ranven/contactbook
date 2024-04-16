
from tkinter import ttk, constants
from services.contact_service import contact_service


class ContactCreationError(Exception):
    pass


class ContactsForm:
    def __init__(self, root, handle_create):
        self._root = root
        self._handle_create = handle_create
        self._frame = None
        self._firstname_entry = None
        self._lastname_entry = None
        self._email_entry = None
        self._phone_entry = None
        self._role_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_handler(self):
        first_name = self._firstname_entry.get()
        last_name = self._lastname_entry.get()
        phone = self._phone_entry.get()

        try:
            contact_service.create_contact(
                first_name, last_name, phone, "", "")
            self._handle_create()
        except ContactCreationError:
            # todo: error handling
            print("Error")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Add new contact")

        self._initialize_firstname_field()
        self._initialize_lastname_field()
        self._initialize_phone_field()

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._create_handler
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._handle_create
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)
        label.grid(row=0, column=0)
        create_button.grid(padx=5, pady=5, sticky=constants.EW)
        cancel_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_firstname_field(self):
        firstname_label = ttk.Label(master=self._frame, text="First Name")
        self._firstname_entry = ttk.Entry(master=self._frame)

        firstname_label.grid(padx=5, pady=5, sticky=constants.W)
        self._firstname_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_lastname_field(self):
        lastname_label = ttk.Label(master=self._frame, text="Last Name")
        self._lastname_entry = ttk.Entry(master=self._frame)

        lastname_label.grid(padx=5, pady=5, sticky=constants.W)
        self._lastname_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_phone_field(self):
        phone_label = ttk.Label(master=self._frame, text="Phone number")
        self._phone_entry = ttk.Entry(master=self._frame)

        phone_label.grid(padx=5, pady=5, sticky=constants.W)
        self._phone_entry.grid(padx=5, pady=5, sticky=constants.EW)
