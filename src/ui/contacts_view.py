from tkinter import Canvas
from tkinter import ttk, constants
from services.user_service import user_service
from services.contact_service import contact_service


class ContactCreationError(Exception):
    pass


class ContactsView:
    def __init__(self, root, handle_logout, handle_create, handle_delete):
        self._root = root
        self._frame = None
        self._canvas = None
        self._scrollbar = None
        self._handle_logout = handle_logout
        self._handle_create = handle_create
        self._handle_delete = handle_delete
        self._contacts = []
        self._contact_form_frame = None
        self._contact_form_view = None
        self._user = user_service.get_current()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _delete_all_handler(self):
        contact_service.delete_all(self._user.id)
        self._handle_delete()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_scrollbar()

        self._contacts = contact_service.get_contacts(self._user.id)

        for contact in self._contacts:
            self._initialize_contact(contact)

    def _initialize_header(self):
        top_frame = ttk.Frame(master=self._frame)
        top_frame.pack(fill=constants.X)

        btn_style = ttk.Style()
        btn_style.map("Red.TButton", background=[
                      ('active', 'red'), ('!active', 'lightgrey')])

        delete_all_button = ttk.Button(
            master=top_frame,
            text="Delete all",
            command=self._delete_all_handler,
            style="Red.TButton"
        )

        delete_all_button.pack(side=constants.RIGHT, padx=5, pady=5)

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

    def _initialize_scrollbar(self):
        self._canvas = Canvas(self._frame)
        self._canvas.pack(side=constants.LEFT,
                          fill=constants.BOTH, expand=True)

        self._scrollbar = ttk.Scrollbar(
            self._frame, orient=constants.VERTICAL, command=self._canvas.yview)
        self._scrollbar.pack(side=constants.RIGHT, fill=constants.Y)
        self._canvas.configure(yscrollcommand=self._scrollbar.set)

        self._inner_frame = ttk.Frame(self._canvas)
        self._canvas.create_window(
            (0, 0), window=self._inner_frame, anchor=constants.NW)

        self._inner_frame.bind("<Configure>", lambda e: self._canvas.configure(
            scrollregion=self._canvas.bbox("all")))

    def _initialize_contact(self, contact):
        style = ttk.Style()
        style.configure("ContactFrame.TFrame", background="white")
        style.configure("ContactLabel.TLabel", background="white")

        contact_frame = ttk.Frame(
            master=self._inner_frame, style="ContactFrame.TFrame")
        contact_frame.config(padding=8, borderwidth=1)

        labels = [
            ("First Name:", contact.first_name, 0, 0, 10),
            ("Last Name:", contact.last_name, 1, 0, 10),
            ("Email:", contact.email, 2, 0, 10),
            ("Phone:", contact.phone, 0, 2, 25),
            ("Role:", contact.role, 1, 2, 25)
        ]

        for label_text, value, row, column, padx_value in labels:
            label = ttk.Label(master=contact_frame,
                              text=label_text, style="ContactLabel.TLabel")
            label.grid(row=row, column=column, sticky="w")

            value_label = ttk.Label(
                master=contact_frame, text=value, style="ContactLabel.TLabel")
            value_label.grid(row=row, column=column + 1, sticky="w",
                             padx=padx_value)

        contact_frame.pack(fill=constants.X, expand=True, padx=10, pady=(5, 0))
