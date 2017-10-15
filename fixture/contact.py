from fixture.creator import CreatorHelper
from model.contact import Contact
from random import randrange

class ContactHelper(CreatorHelper):

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        # Go to contact creator
        wd.find_element_by_link_text("nowy wpis").click()
        self.fill_contact_form(contact)
        # Submit to add new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.surename)
        self.change_field_value("address", contact.address)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Click delete
        wd.find_element_by_xpath("//*[@value='Usuń']").click()
        # Accept deletion
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Click edit
        wd.find_element_by_xpath("//*[@title='Edytuj']").click()
        self.fill_contact_form(new_contact_data)
        # Submit edition
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def count_of_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            i = 2  # because first element is in row nr = 2
            for row in wd.find_elements_by_name("selected[]"):
                # i-th row td 2nd and 3rd
                last_name = wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[%d]/td[2]" % i).text
                first_name = wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[%d]/td[3]" % i).text
                contact_id = row.get_attribute("value")
                self.contact_cache.append(Contact(firstname=first_name, surename=last_name, contact_id=contact_id))
                i += 1  # making iterator +1 for next row in loop
        return list(self.contact_cache)
