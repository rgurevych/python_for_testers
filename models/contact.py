from sys import maxsize


class Contact:
    def __init__(self, first_name=None, last_name=None, mobile_phone=None, home_phone = None,
                 work_phone = None, fax = None, email=None, id=None, address = None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.address = address
        self.id = id


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)


    def contact_id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
