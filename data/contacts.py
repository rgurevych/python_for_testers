import random
import string
import re
from models.contact import Contact

def random_string(max_length):
    sym = string.ascii_letters + string.digits + " "*10
    return re.sub('\s+', ' ', ("".join([random.choice(sym) for i in range(random.randrange(3, max_length))]).strip()))


def random_email():
    domen = [".com", ".org", ".ua", ".de", ".co.uk", ".gov", ".eu", ".tv"]
    return re.sub('\s+', '', random_string(10)) + "@" + re.sub('\s+', '',random_string(10)) + random.choice(domen)


def random_phone():
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(6, 12))])


def random_address():
    return random_string(20) + "\n" + random_string(20) + "\n" + random_string(20)


testdata = [Contact(first_name="", last_name="", email_1="", mobile_phone="", address="")] + [
           Contact(first_name=random_string(10), last_name=random_string(15),
                   mobile_phone=random_phone(), work_phone=random_phone(), home_phone=random_phone(), fax=random_phone(),
                   email_1=random_email(), email_2=random_email(), email_3=random_email(), address=random_address())
           for i in range(5)
           ]

empty_contact_data = [Contact(first_name="", last_name="", email_1="", mobile_phone="", address="")]

default_contact_data = [Contact(first_name="Firstname", last_name="Lastname", mobile_phone="+12345678",
                                work_phone="12345", home_phone="67890", fax="55443322", email_1="email_1@email.com",
                                email_2="email_2@email.com", email_3="email_3@email.com",
                                address="Street, 15 \n 12345 New-York")]