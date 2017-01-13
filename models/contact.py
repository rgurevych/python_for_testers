from sys import maxsize


class Contact:
    def __init__(self, first_name=None, last_name=None, mobile_phone=None, home_phone=None, all_emails_homepage=None,
                 work_phone=None, fax=None, email_1=None, email_2=None, email_3=None, id=None, address=None,
                 all_phones_homepage = None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.all_phones_homepage = all_phones_homepage
        self.all_emails_homepage = all_emails_homepage
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
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
