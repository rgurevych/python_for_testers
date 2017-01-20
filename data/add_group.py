import string
import random
import re
from models.group import Group

default_group_data = [Group(name="Name_1", header="Header_1", footer="Footer_1")]

emptry_group_data = [Group(name="", header="", footer="")]

def random_string(prefix, max_length):
    sym = string.ascii_letters + string.digits + " "*20
    #The following string generates random string, replaces duplicated spaces with only one and deletes space in the end
    return re.sub('\s+', ' ', (prefix + "".join([random.choice(sym)
                                                 for i in range(random.randrange(max_length))]).rstrip()))


testdata = [Group(name="", header="", footer="")] + [
           Group(name=random_string("name", 10), header=random_string("head", 15), footer=random_string("foot", 15))
           for i in range(5)
           ]
