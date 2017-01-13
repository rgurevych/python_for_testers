import re
from models.contact import Contact
from random import randrange


def test_contact_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Mister", last_name="Muster", mobile_phone="123", email_1="test@test.com"))
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_editpage = app.contact.get_contact_data_editpage(index)
    assert contact_from_homepage.first_name == contact_from_editpage.first_name
    assert contact_from_homepage.last_name == contact_from_editpage.last_name
    assert contact_from_homepage.address == contact_from_editpage.address
    assert contact_from_homepage.all_phones_homepage == merge_phones_homepage(contact_from_editpage)
    assert contact_from_homepage.all_emails_homepage == merge_emails_homepage(contact_from_editpage)


"""def test_phones_on_viewpage(app):
    contact_from_viewpage = app.contact.get_contact_data_viewpage(0)
    contact_from_editpage = app.contact.get_contact_data_editpage(0)
    assert contact_from_viewpage.home_phone == contact_from_editpage.home_phone
    assert contact_from_viewpage.work_phone == contact_from_editpage.work_phone
    assert contact_from_viewpage.mobile_phone == contact_from_editpage.mobile_phone
    assert contact_from_viewpage.fax == contact_from_editpage.fax"""


def clear(s):
    #return "".join(symbol for symbol in s if symbol not in "[]()- 0")
    return re.sub("[- ()]", "", s)


def merge_phones_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))

def merge_emails_homepage(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email_1, contact.email_2, contact.email_3])))
