import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.contact_homephone == clear(contact_from_edit_page.contact_homephone)
    assert contact_from_home_page.contact_mobilephone == clear(contact_from_edit_page.contact_mobilephone)
    assert contact_from_home_page.contact_workphone == clear(contact_from_edit_page.contact_workphone)
    assert contact_from_home_page.contact_secondaryphone == clear(contact_from_edit_page.contact_secondaryphone)


def clear(s):
    return re.sub("[() -]", "", str(s))
