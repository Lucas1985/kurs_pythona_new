class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        # Go to contact creator
        wd.find_element_by_link_text("nowy wpis").click()
        # Fill the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surename)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address)
        # Submit to add new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Click delete
        wd.find_element_by_xpath("//*[@value='Usuń']").click()
        # Accept deletion
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # Select first contact
        wd.find_element_by_name("selected[]").click()
        # Click edit
        wd.find_element_by_xpath("//*[@title='Edytuj']").click()
        # Fill the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surename)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address)
        # Submit edition
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()