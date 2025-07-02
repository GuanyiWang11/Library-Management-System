import csv
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk #it is a submodule so cant be imported with the first line

class Library:

    def __init__(self, collection):
        self.collection = collection
        self.name = "Library"
        self.main_window = None
        self.sorted = False
        self.searched = False
        
    # runs and displays window
    def open_(window):
        library.main_window.mainloop()
    
class Book:
    
    def __init__(self, 
                ID, title, author, 
                genre, available):

        self.ID = int(ID)
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
    
    # return sort value: ID or title
    def get_sort_value(self, value):
        
        value = value.lower() # convert to lowercase
        
        if value == "id":
            return self.ID
        
        elif value == "title":
            return self.title
        
        elif value == "author":
            
            return self.author
        
        elif value == "genre":
            return self.genre

# set layout to get sort by 
def sort():
    
    clear()
    library.searched = False
    global sort_by_var
    sort_by_var = StringVar()
    
    label = Label(main_frame, text="Sort by:")
    entry = Entry(main_frame, textvariable=sort_by_var)
    submit_button= Button(main_frame, text="Submit", command=sort_submit)
        
    label.pack()
    entry.pack()
    submit_button.pack()
    
def sort_submit():
    
    # get name of sort
    global sort_by
    sort_by = sort_by_var.get()
    
    if not validate_sort_by(sort_by):
        messagebox.showerror("Invalid input", "Input must either id, title, author, or genre")
    
    else:
        library.sorted = True
        
        n = len(books)
        for i in range(n):
            for j in range(n-1):
                if books[j].get_sort_value(sort_by) > books[j+1].get_sort_value(sort_by):
                    books[j], books[j+1] = books[j+1], books[j]
        load()
     # automatically reset input box to blank

def validate_sort_by(sort_by):
    if sort_by.lower() in ["id", "title", "author", "genre"]:
        return True
    else:
        return False
    
def search():
    clear()
    global search_var, search
    search_var = StringVar()
    
    if library.sorted == True and sort_by.lower() == "title":
        
        label = Label(main_frame, text="Search:")
        entry = Entry(main_frame, textvariable=search_var) #this gives the actual input box
        submit_button= Button(main_frame, text="Submit", command=search_submit)
        
        label.pack()
        entry.pack()
        submit_button.pack() 
        
    else:
        messagebox.showerror("Execution Error", "Must be sorted first by title")
        
def search_submit():
    global search_pos, search
    search = search_var.get()
    low = 0
    high = len(books) - 1
    mid = 0
    found = False
    

    while low <= high and found == False:
        mid = (high + low) // 2
            
        # if search_var is greater, ignore left half
        if books[mid].title < search:
            low = mid + 1

        # if search_var is smaller, ignore right half
        elif books[mid].title > search:
            high = mid - 1

        # means search_var is present at mid
        else:
            library.searched = True
            search_pos = mid
            load()
            found = True
                
    if found == False:
        messagebox.showerror("Error", "Can't find book")

def borrow():
    clear()
    global borrow_var
    borrow_var = StringVar()

    label = Label(main_frame, text="Borrow: ")
    entry = Entry(main_frame, textvariable=borrow_var)
    submit_button= Button(main_frame, text="Submit", command=borrow_submit)
        
    label.pack()
    entry.pack()
    submit_button.pack() 
        

def borrow_submit():

    borrow = borrow_var.get()
    found = False
    counter = 0
    
    while found == False and counter < len(books):
        
        if books[counter].title == borrow:
            if books[counter].available == "Yes":
                label = Label(main_frame, text=(borrow, "borrowed"))
                books[counter].available = "No"
                label.pack()
                
            elif books[counter].available == "No":
                messagebox.showerror("Error", "Book unavailable")
                
            found = True
            
        counter += 1
    
    if found == False:
        messagebox.showerror("Error", "Book cannot be found within the library")
    
    
def return_():
    clear()
    global return_var
    return_var = StringVar()

    label = Label(main_frame, text="Return: ")
    entry = Entry(main_frame, textvariable=return_var) #this gives the actual input box
    submit_button= Button(main_frame, text="Submit", command=return_submit)
        
    label.pack()
    entry.pack()
    submit_button.pack() 

def return_submit():
    return_ = return_var.get()
    found = False
    counter = 0
    
    while found == False and counter < len(books):
        
        if books[counter].title == return_:
            
            if books[counter].available == "No":
                label = Label(main_frame, text=(return_, "returned"))
                books[counter].available = "Yes"
                label.pack()
                
            elif books[counter].available == "Yes":
                messagebox.showerror("Error", "Book is already available. Are you sure its this book you want to return?")
            
            found = True
            
        counter += 1
    
    if found == False:
        messagebox.showerror("Error", "Book cannot be found within the library")


    
def load():
    clear()
    #sets empty treeview, and label
    label = Label(main_frame, text="Books:")
    treeview = ttk.Treeview(
                            main_frame,
                            columns=("ID", "Title", "Author", "Genre","Available"),
                            show="headings"
                            )
    treeview.heading("ID", text="ID")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Genre", text="Genre")
    treeview.heading("Available", text="Available")
    
    items = []
    
    for book in books:
        item_id = treeview.insert(
                                "",
                                END,
                                values=(
                                         book.ID, book.title, book.author,
                                         book.genre, book.available))
        items.append(item_id)
    if library.searched:
        book = books[search_pos]
        treeview.item(items[search_pos], values=(book.ID, book.title.upper(), book.author.upper(),
                                         book.genre.upper(), book.available.upper()))
    
    label.pack()
    treeview.pack()

def clear():
    for widget in main_frame.winfo_children():
        widget.destroy()
        
def save():

    file_edit = open("book.csv", "w", newline= "")
    writer = csv.writer(file_edit)

    for row in books:
        writer.writerow([row.ID, row.title, row.author, row.genre, row.available])
                            
    file_edit.close()

def csv_to_array(file_name):
    
    array = []
    file = open(file_name, "r")


    for row in csv.reader(file):
        array.append(Book(
                            row[0],row[1],
                            row[2],row[3], row[4]
                            ))

    file.close()

    return array

def create_window(library_name):
    window = Tk()
    window.geometry("1000x500")
    window.title("Library")


    # sets parallel arrays of button info
    btn_names = [
       "sort","search","borrow",
       "return","load","save"
        ]

    btn_funcs = [
        sort,search,borrow,
        return_,load,save
        ]

    # creates every button
    frame = Frame(window)
    frame.pack()
    n = len(btn_names)
    for i in range(n):
        btn = Button(frame, text=btn_names[i], command=btn_funcs[i])
        btn.pack(side=LEFT)
    
    return window

def main():
    global books
    books = csv_to_array("book.csv")
     
    global library
    library = Library(books) # creates library
    library.main_window = create_window(library) # creates main window of that library
    global main_frame
    #if "main_frame" in globals() and main_frame.winfo_exists():
       # main_frame.destroy()
    main_frame = Frame(library.main_window)
    main_frame.pack()
    library.open_() #d isplays main window

#  main Program
main()
