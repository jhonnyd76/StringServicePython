import mysql.connector
from xml.dom import minidom


class DbConnection:
    def __init__(self):
        self.dataspace = None
        self.customer = None
        self.credentials = None
        credentials = self.readXML()
        self.connection = mysql.connector.connect(host=credentials[0][0],
                                                  database=credentials[0][1],
                                                  user=credentials[0][2],
                                                  password=credentials[0][3])

    def getCustomers(self):
        self.dataspace = {}
        self.customer = []
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM tbl_customers''')
        rows = cursor.fetchall()
        for row in rows:
            id = row[0]
            name = row[1]
            firstname = row[2]
            mail = row[5]
            self.customer.append([id, name, firstname, mail])
        return self.customer

    def getCustomer(self, customerID):
        self.dataspace = {}
        self.customer = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tbl_customers WHERE customers_id = '%s'" % customerID)
        rows = cursor.fetchall()
        for row in rows:
            id = row[0]
            name = row[1]
            firstname = row[2]
            intPhone = row[3]
            phoneNr = row[4]
            mail = row[5]
            streetName = row[6]
            streetNr = row[7]
            postalCode = row[8]
            city = row[9]
            self.customer.append([id, name, firstname, intPhone, phoneNr, mail, streetName, streetNr, postalCode, city])
        return self.customer

    def readXML(self):
        self.credentials = []
        myDoc = minidom.parse('sql/credentials.xml')
        items = myDoc.getElementsByTagName('item')
        server = items[0].firstChild.data
        database = items[1].firstChild.data
        username = items[2].firstChild.data
        password = items[3].firstChild.data
        self.credentials.append([server,database,username,password])
        #print(self.credentials)
        return self.credentials


