
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.contacts_view import ContactsView
from ui.contact_form_view import ContactsForm


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._root.configure(background="grey")
        self._root.minsize(500, 500)
        self._show_login_view()

    def _destroy_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._show_contacts_view,
            self._show_register_view
        )
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(
            self._root,
            self._show_contacts_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_contacts_view(self):
        self._hide_current_view()
        self._current_view = ContactsView(
            self._root, self._show_login_view, self._show_contact_form_view)
        self._current_view.pack()

    def _show_contact_form_view(self):
        self._hide_current_view()
        self._current_view = ContactsForm(
            self._root, self._show_contacts_view)
        self._current_view.pack()
