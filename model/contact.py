from sys import maxsize


class Contact:

    def __init__(self,
                 contact_first_name=None,
                 contact_last_name=None,
                 contact_id=None,
                 contact_homephone = None,
                 contact_mobilephone = None,
                 contact_workphone = None,
                 contact_secondaryphone = None):
        self.contact_first_name = contact_first_name
        self.contact_last_name = contact_last_name
        self.contact_homephone = contact_homephone
        self.contact_mobilephone = contact_mobilephone,
        self.contact_workphone = contact_workphone,
        self.contact_secondaryphone = contact_secondaryphone
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.contact_first_name, self.contact_last_name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
            and (self.contact_first_name is None or other.contact_first_name is None or self.contact_first_name == other.contact_first_name) \
            and (self.contact_last_name is None or other.contact_last_name is None or self.contact_last_name == other.contact_last_name)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
