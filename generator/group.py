import string
import random
import re
import os.path
import jsonpickle
import getopt
import sys
from models.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, max_length):
    sym = string.ascii_letters + string.digits + " "*20
    #The following string generates random string, replaces duplicated spaces with only one and deletes space in the end
    return re.sub('\s+', ' ', (prefix + "".join([random.choice(sym)
                                                 for i in range(random.randrange(max_length))]).rstrip()))


testdata = [Group(name="", header="", footer="")] + [
           Group(name=random_string("name", 10), header=random_string("head", 15), footer=random_string("foot", 15))
           for i in range(n)
           ]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(data_file, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))