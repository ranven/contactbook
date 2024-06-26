from tkinter import ttk, constants, StringVar
from services.contact_service import contact_service, ContactCreationError, PhoneNumberError
from services.user_service import user_service


class ContactsForm:
    """Luokka joka vastaa kontaktin luomisen käyttöliittymätoteutuksesta.
    """

    def __init__(self, root, handle_create):
        self._root = root
        self._handle_create = handle_create
        self._frame = None
        self._firstname_entry = None
        self._lastname_entry = None
        self._email_entry = None
        self._phone_entry = None
        self._role_entry = None
        self._error_variable = None
        self._error_label = None
        self._user = user_service.get_current_user()

        self._initialize()

    def pack(self):
        """Pakkaa näkymän komponentit isäntäkomponentin sisään.
        """
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        """Tuhoaa näkymän komponentit."""
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _create_handler(self):
        first_name = self._firstname_entry.get()
        last_name = self._lastname_entry.get()
        phone = self._phone_entry.get()
        email = self._email_entry.get()
        role = self._role_entry.get()
        try:
            contact_service.create_contact(
                first_name, last_name, email, phone, role, self._user.id)
            self._handle_create()

        except PhoneNumberError:
            self._show_error(
                "Phone number should only contain numbers from 0 to 9")

        except ContactCreationError:
            self._show_error(
                "Each field has a maximum length of 100 characters.")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        label = ttk.Label(master=self._frame, text="Add new contact")

        self._initialize_firstname_field()
        self._initialize_lastname_field()
        self._initialize_email_field()
        self._initialize_phone_field()
        self._initialize_role_field()

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

    def _initialize_email_field(self):
        email_label = ttk.Label(master=self._frame, text="Email")
        self._email_entry = ttk.Entry(master=self._frame)

        email_label.grid(padx=5, pady=5, sticky=constants.W)
        self._email_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_role_field(self):
        role_label = ttk.Label(master=self._frame, text="Role")
        self._role_entry = ttk.Entry(master=self._frame)

        role_label.grid(padx=5, pady=5, sticky=constants.W)
        self._role_entry.grid(padx=5, pady=5, sticky=constants.EW)
