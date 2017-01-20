import random
import string
import re
import os.path
import json
import getopt
import sys
from models.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
           for i in range(n)
           ]


data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(data_file, "w") as f_out:
    f_out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))