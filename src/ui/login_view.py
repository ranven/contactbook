from tkinter import ttk, StringVar, constants
from services.user_service import user_service


class LoginView:
    def __init__(self, root, handle_login, handle_show_register_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_register_view = handle_show_register_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self._handle_login()
        except:
            print("incorrect username or password")
            # todo: error handling

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_username_field()
        self._initialize_password_field()

        label = ttk.Label(master=self._frame, text="Log in")

        login_button = ttk.Button(
            master=self._frame, text="Log in", command=self._login_handler)

        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._handle_show_register_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=600)

        label.grid(row=0, column=0)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        register_button.grid(padx=5, pady=5, sticky=constants.EW)
