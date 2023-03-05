class Contact:

    def __init__(self, contact_first_name=None, contact_last_name=None, contact_id=None):
        self.contact_first_name = contact_first_name
        self.contact_last_name = contact_last_name
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.contact_first_name, self.contact_last_name)

    def __eq__(self, other):
        return self.contact_id == other.contact_id \
            and self.contact_first_name == other.contact_first_name \
            and self.contact_last_name == other.contact_last_name
