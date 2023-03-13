import re
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_details_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_details_page.contact_homephone == contact_from_edit_page.contact_homephone
    assert contact_from_details_page.contact_mobilephone == contact_from_edit_page.contact_mobilephone
    assert contact_from_details_page.contact_workphone == contact_from_edit_page.contact_workphone
    assert contact_from_details_page.contact_secondaryphone == contact_from_edit_page.contact_secondaryphone


def test_verify_all_contact_data_in_edit_view(app):
    contacts_list_on_home_page = app.contact.get_contacts_list()
    index = randrange(len(contacts_list_on_home_page))
    random_contact_from_home_page = app.contact.get_contacts_list()[index]
    random_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert random_contact_from_home_page.contact_id \
           == random_contact_from_edit_page.contact_id
    assert random_contact_from_home_page.contact_first_name \
           == random_contact_from_edit_page.contact_first_name
    assert random_contact_from_home_page.contact_last_name \
           == random_contact_from_edit_page.contact_last_name
    assert random_contact_from_home_page.contact_main_address \
           == random_contact_from_edit_page.contact_main_address
    assert \
        random_contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
            random_contact_from_edit_page)
    assert \
        random_contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
            random_contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", str(s))


def merge_emails_like_on_home_page(contact):
    return "\n".join(
                          [
                              contact.contact_first_email,
                              contact.contact_second_email,
                              contact.contact_third_email
                          ]
                   )


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [
                              contact.contact_homephone,
                              contact.contact_workphone,
                              contact.contact_mobilephone,
                              contact.contact_secondaryphone
                          ]
                          )
                   )
               )
    )
