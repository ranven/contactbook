from tkinter import ttk, StringVar, constants
from services.user_service import user_service, InvalidCredentialsError


class RegisterView:
    def __init__(self, root, handle_register, handle_show_login_view):
        self._root = root
        self._handle_register = handle_register
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _register_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            print("Username and password are required")
            # todo: error handling
            return

        try:
            user_service.create(username, password)
            self._handle_register()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password.")

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username_requirements = ttk.Label(
            master=self._frame, font=("Arial", 10), foreground="#5A5A5A", text="Username needs to be unique and at least 4 characters long")

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)
        username_requirements.grid(padx=5, pady=5, sticky=constants.W)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.config(show="*")

        password_requirements = ttk.Label(
            master=self._frame, font=("Arial", 10), foreground="#5A5A5A", text="Password needs to be at least 4 characters long")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)
        password_requirements.grid(padx=5, pady=5, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._initialize_username_field()
        self._initialize_password_field()

        label = ttk.Label(master=self._frame, text="Register new user")

        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._register_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Log in",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

        label.grid(row=0, column=0)
        register_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
