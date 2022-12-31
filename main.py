from tkinter import *
from tkinter import ttk
from sql.connection import DbConnection
from tkinter import Menu
import additional.menuAction as menuAction


def fillCustomers():
    customerList.delete(0, END)
    dbcon = DbConnection()
    customers = dbcon.getCustomers()
    for customer in customers:
        customerList.insert(END, str(customer[0]) + " " + customer[1] + " " + customer[2])


def setCustomer(userID):
    dbcon = DbConnection()
    customers = dbcon.getCustomer(userID)
    for customer in customers:
        customerName.set(customer[1])
        customerFirstName.set(customer[2])
        customerPhone.set(customer[3] + customer[4])
        customerMail.set(customer[5])
        customerStreetName.set(customer[6])
        customerStreetNr.set(customer[7])
        customerPLZ.set(customer[8])
        customerCity.set(customer[9])


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    values = w.get(index)
    value = values.split(" ")
    setCustomer(value[0])


root = Tk()
menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0)
customerMenu = Menu(menubar, tearoff=0)
stringMenu = Menu(menubar, tearoff=0)
orderMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="new File", command=menuAction.newFile)
fileMenu.add_command(label="open File", command=menuAction.openFile)
customerMenu.add_command(label="new Customer", command=menuAction.newCustomer)
stringMenu.add_command(label="new String", command=menuAction.newString)
orderMenu.add_command(label="new Order", command=menuAction.newOrder)

menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Customers", menu=customerMenu)
menubar.add_cascade(label="Strings", menu=stringMenu)
menubar.add_cascade(label="Orders", menu=orderMenu)

customerName = StringVar()
customerFirstName = StringVar()
customerMail = StringVar()
customerPhone = StringVar()
customerStreetNr = StringVar()
customerStreetName = StringVar()
customerPLZ = StringVar()
customerCity = StringVar()

nb = ttk.Notebook(root)
nb.pack(fill=BOTH)
cusDB = Frame(nb, bg="green")
stringDB = Frame(nb, bg="yellow")
orderDB = Frame(nb, bg="purple")
"""
NewCustomerBtn = Button(nb, text="New Customer", width=20)
CancelBtn = Button(nb, text="Cancel", width=20, command=root.destroy)
NewCustomerBtn.pack(side=LEFT)
CancelBtn.pack(side=RIGHT)
"""

customerListFrame = Frame(cusDB)
customerInfoFrame = Frame(cusDB)
customerOrdersFrame = Frame(cusDB)

customerNameLabel = Label(customerInfoFrame, text="Name", width=25)
customerNameEntry = Entry(customerInfoFrame, textvariable=customerName, width=25, state=DISABLED)
customerFirstNameLabel = Label(customerInfoFrame, text="Vorname", width=25)
customerFirstNameEntry = Entry(customerInfoFrame, textvariable=customerFirstName, width=25, state=DISABLED)
customerAdresseStreetLabel = Label(customerInfoFrame, text="Strasse", width=25)
customerAdresseStreetEntry = Entry(customerInfoFrame, textvariable=customerStreetName, width=25, state=DISABLED)
customerAdresseNrLabel = Label(customerInfoFrame, text="Hausnummer", width=25)
customerAdresseNrEntry = Entry(customerInfoFrame, textvariable=customerStreetNr, width=25, state=DISABLED)
customerCityNummerLabel = Label(customerInfoFrame, text="PLZ", width=25)
customerCityNummerEntry = Entry(customerInfoFrame, textvariable=customerPLZ, width=25, state=DISABLED)
customerCityNameLabel = Label(customerInfoFrame, text="Ortschaft", width=25)
customerCityNameEntry = Entry(customerInfoFrame, textvariable=customerCity, width=25, state=DISABLED)
customerMailLabel = Label(customerInfoFrame, text="e-Mail", width=25)
customerMailEntry = Entry(customerInfoFrame, textvariable=customerMail, width=25, state=DISABLED)
customerPhoneLabel = Label(customerInfoFrame, text="Phone", width=25)
customerPhoneEntry = Entry(customerInfoFrame, textvariable=customerPhone, width=25, state=DISABLED)

customerListFrame.grid(row=0, column=0, rowspan=10, pady=10, padx=10)
customerInfoFrame.grid(row=0, column=1, columnspan=4, pady=10, padx=10)
customerOrdersFrame.grid(row=0, column=5, rowspan=10, padx=10, pady=10)
customerNameLabel.grid(row=0, column=0)
customerFirstNameLabel.grid(row=0, column=1)
customerNameEntry.grid(row=1, column=0)
customerFirstNameEntry.grid(row=1, column=1)
customerAdresseStreetLabel.grid(row=2, column=0)
customerAdresseNrLabel.grid(row=2, column=1)
customerAdresseStreetEntry.grid(row=3, column=0)
customerAdresseNrEntry.grid(row=3, column=1)
customerCityNummerLabel.grid(row=4, column=0)
customerCityNameLabel.grid(row=4, column=1)
customerCityNummerEntry.grid(row=5, column=0)
customerCityNameEntry.grid(row=5, column=1)
customerMailLabel.grid(row=6, column=0)
customerPhoneLabel.grid(row=6, column=1)
customerMailEntry.grid(row=7, column=0)
customerPhoneEntry.grid(row=7, column=1)


customerList = Listbox(customerListFrame, height=100, width=30)
customerList.pack()
customerList.bind('<<ListboxSelect>>', onselect)

orderList = Listbox(customerOrdersFrame, height=100, width=30)
orderList.pack()


"""
name = TextFrames(customerFrame, "Name:", 0, 0, 1, 0)
firstName = TextFrames(customerFrame, "Vorname:", 0, 1, 1, 1)
id = TextFrames(self.customerFrame, "ID:", 0, 2, 1, 2)
"""

nb.add(cusDB, text="Customers DB")
nb.add(stringDB, text="Strings DB")
nb.add(orderDB, text="Order DB")
fillCustomers()

root.attributes("-fullscreen", True)
root.title("String Service")
root.config(menu=menubar)
root.mainloop()
