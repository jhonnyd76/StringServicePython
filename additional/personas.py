class Customer:
    def __init__(self, id, name, firstname):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.mail = None

    def setCustomer(self, id, name, firstname, mail):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.mail = mail
