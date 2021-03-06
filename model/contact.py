from sys import maxsize

class Contact:

    def __init__(self, firstname=None, surename=None, address=None, contact_id=None):
        self.firstname = firstname
        self.surename = surename
        self.address = address
        self.contact_id = contact_id


    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.firstname, self.surename)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)\
               and self.firstname == other.firstname and self.surename == other.surename

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize