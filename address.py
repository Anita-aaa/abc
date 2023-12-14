from tkinter import *
import sqlite3

root =Tk()
root.title("Database Address Book")

# Database

# Create a database or connect to one
conn=sqlite3.connect("address_book.db")


# cursur creating
# execute any query we entry in the box
c=conn.cursor()

#create table
c.execute(""" CREATE TABLE address(
        first_name text,
        last_name text,
        address text,
        city text
        zipcode integer
)""")
print ("table created successfully")
#commit change

def submit():
    # clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create text boxes
f_name =Entry(root,width =30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)

state=Entry(root,width=30)
state.grid(row=3,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=4,column=1)

# Create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label =Label(root,text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root,text="Address")
address_label.grid(row=2, column=0)

city_label =Label(root,text="City")
city_label.grid(row=3,column=0)

state_label= Label(root,text="State")
state_label.grid(row=3, column=0)

# Create submit button
submit_btn =Button(root,text="Add Records", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# commit change
conn.commit()

# cloae connection
conn.close()

root.mainloop()



