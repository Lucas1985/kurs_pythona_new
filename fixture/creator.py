class CreatorHelper:

    def __init(self, app):
        self.app = app


    def change_field_value(self, field_value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_value).click()
            wd.find_element_by_name(field_value).clear()
            wd.find_element_by_name(field_value).send_keys(text)

    def select_first_checkbox(self):
       wd = self.app.wd
       wd.find_element_by_name("selected[]").click()