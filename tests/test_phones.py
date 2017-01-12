
def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_editpage = app.contact.get_contact_data_editpage(0)
    assert contact_from_homepage.home_phone == contact_from_editpage.home_phone
    assert contact_from_homepage.work_phone == contact_from_editpage.work_phone
    assert contact_from_homepage.mobile_phone == contact_from_editpage.mobile_phone
    #assert contact_from_homepage.fax == contact_from_editpage.fax