from fixture.creator import CreatorHelper

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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.surename)
        self.change_field_value("address", contact.address)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_checkbox()
        # Click delete
        wd.find_element_by_xpath("//*[@value='Usuń']").click()
        # Accept deletion
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_checkbox()
        # Click edit
        wd.find_element_by_xpath("//*[@title='Edytuj']").click()
        self.fill_contact_form(new_contact_data)
        # Submit edition
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def count_of_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))