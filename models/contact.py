
class Contact:
    def __init__(self, first_name=None, last_name=None, mobile_phone=None, email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.email = email
        self.id = id


    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)