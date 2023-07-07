from tkinter import *
from tkinter import ttk 

groceryList = open(r"C:\Users\SERN_INTERN\Desktop\Python Training VSC\database.txt", "r")
groceryList = (groceryList.read())
print (groceryList)

grocery = []
groceryItem = []
groceryItem3 = []

class stuff:
    def __init__(name, item, quantity, price):
        name.item = item
        name.quantity = quantity
        name.price = price
        
def calc():
    i = 0
    for x in range(len(grocery)):
        try:
            qu = float(groceryItem[x])
            pr = float(groceryItem3[x])
            answer = qu * pr
            i = answer + i
            
        except ValueError:
            continue
    entry4.delete(0, END)
    entry4.insert(0, "$" + str(i) )
          
def remove():
    try:
        a = tree.selection()
        print(a)
        ap = (grocery.index(a[0]))
        grocery.remove(a[0])
        groceryItem.remove(groceryItem[ap])
        groceryItem3.remove(groceryItem3[ap])
        tree.delete(tree.selection())
        calc()
    except IndexError:
        return
    
root = Tk()
root.title("Today's Grocery List")
root.geometry("900x900")

label = Label(root, text = "Today's Grocery List:", font=("Arial Black", 40, "bold", "italic", "underline"))
label.pack()
label.pack(pady=25)

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings', height=25)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Item")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Quantity")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Price")
tree.pack()
label = Label(root, text="Item:")
label.pack()
content = StringVar()
entry1 = Entry(root, textvariable=content)
entry1.pack()
label = Label(root, text="Quantity: ")
label.pack()
content = StringVar()
entry2 = Entry(root, textvariable=content)
entry2.pack()

label = Label(root, text="Price:")
label.pack()
content = StringVar()
entry3 = Entry(root, textvariable=content)
entry3.pack()

label = Label(root, text="Total:")
label.pack()
content = StringVar()
entry4 = Entry(root, textvariable=content)
entry4.pack()

def add():
    if entry1.get() == "":
        return
    it = stuff(entry1.get(), entry2.get(), entry3.get())
    for i in range(len(grocery)):
        if grocery[i] == entry1.get():
            tree.delete([entry1.get])
            tree.insert("", i, iid= entry1.get(), values = (entry1.get(), entry2.get(), entry3.get()))
            groceryItem[i] = entry2.get()
            groceryItem3[1] = entry3.get()
            calc()
            remove()
            return
        
    grocery.append(entry1.get())
    groceryItem.append(entry2.get())
    groceryItem3.append(entry3.get())
    tree.insert("", END , iid= entry1.get(), values = (entry1.get(), entry2.get(), "$" + entry3.get()))
    calc()
    remove()

button1 = Button(root, text="Add", command = add)
button1.pack(pady=10)

button2 = Button(root, text="Delete", command = remove)
button2.pack(pady=10)



global my_label
my_label = Label(root, text= " ")
my_label.pack(pady=5)

root.mainloop()
