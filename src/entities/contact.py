class Contact:
    def __init__(self, contact_id, first_name, last_name, email,
                 phone, role, created_at, user):
        self.id = contact_id,
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.role = role
        self.created_at = created_at
        self.user = user
