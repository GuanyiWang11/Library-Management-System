import csv
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk 

class Library:

    def __init__(self, collection):
        self.collection = collection
        self.name = "Andy's Library"
        self.main_window = None
        self.sorted_by_title = False
        self.searched = False
        
    # Runs the main window of library
    def open_(library):
        library.main_window.mainloop()

class Book:
    
    def __init__(self, ID, title, 
                author, genre, available):
        self.ID = int(ID)
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
    

    def get(self, value):
        
        value = value.lower()

        if value == "id":
            return self.ID
        elif value == "title":
            return self.title
        elif value == "author":  
            return self.author
        elif value == "genre":
            return self.genre

def create_window(library):

    window = Tk()
    window.geometry("1000x500")
    window.title(library.name)

    return window

def create_buttons(window, button_info):
    """
    Returns a window with a row of buttons
    """

    for x, y in button_info.items():
        button = Button(button_frame, text=x, command=y)
        button.pack(side=LEFT)
    
    return window  

def sort():
    """
    Displays input box to get value to be sorted by
    """
    clear(input_frame)

    library.searched = False
    sort_var = StringVar()

    label = Label(input_frame, text="Sort by:")
    entry = Entry(input_frame, textvariable=sort_var)
    submit_button = Button(input_frame, text="Submit", command=lambda: sort_submit(sort_var))
        
    label.pack()
    entry.pack()
    submit_button.pack()
    
def sort_submit(var):
    """
    Displays bubble-sorted list of books by sort by value as inputted by user
    """
    sort_val = var.get()
    
    if validate_sort_val(sort_val):
        
        n = len(books)

        for i in range(n):

            for j in range(n-1):

                if books[j].get(sort_val) > books[j+1].get(sort_val):
                    books[j], books[j+1] = books[j+1], books[j]
        load()
    
    else:
        messagebox.showerror("Error", "Input must either id, title, author, or genre")
    
def validate_sort_val(sort_val):

    if sort_val.lower() in ["id", "title", "author", "genre"]:

        if sort_val.lower() == "title":
            library.sorted_by_title = True

        return True
    else:
        print(sort_val)
        return False
    
def search():
    """
    Displays input box to get a value to search for
    """

    clear(input_frame)

    search_var = StringVar()
    
    if library.sorted_by_title:
        
        label = Label(input_frame, text="Search:")
        entry = Entry(input_frame, textvariable=search_var) # This gives the actual input box
        submit_button= Button(input_frame, text="Submit", command=lambda: search_submit(search_var))
        
        label.pack()
        entry.pack()
        submit_button.pack() 
        
    else:
        messagebox.showerror("Error", "Library must be sorted by title before search")
        
def search_submit(var):
    """
    Highlights search book inputted by user through a binary search
    """
    global search_pos

    search_val = var.get()

    low = 0
    high = len(books) - 1
    mid = 0
    found = False

    while low <= high and found == False:
        mid = (high + low) // 2
            
        # If search_var is greater, ignore left half
        if books[mid].title < search_val:
            low = mid + 1

        # If search_var is smaller, ignore right half
        elif books[mid].title > search_val:
            high = mid - 1

        # Means search_var is present at mid
        else:
            library.searched = True
            search_pos = mid
            load()
            found = True
                
    if found == False:
        messagebox.showerror("Error", f"{search_val} cannot be found within library")

def borrow():
    """
    Displays input box to get book to be borrowed
    """

    clear(input_frame)

    borrow_var = StringVar()

    label = Label(input_frame, text="Borrow: ")
    entry = Entry(input_frame, textvariable=borrow_var)
    submit_button= Button(input_frame, text="Submit", command=lambda: borrow_submit(borrow_var))
        
    label.pack()
    entry.pack()
    submit_button.pack() 
        
def borrow_submit(var):
    """
    Changes books availbility if book is available
    """
    borrow_val = var.get()
    found = False
    counter = 0
    
    # Loops through every item unless book is found
    while found == False and counter < len(books):
        
        if books[counter].title == borrow_val:

            if books[counter].available == "Yes":
                messagebox.showinfo("Library Updated", f"{borrow_val} is borrowed")
                books[counter].available = "No"
                
            elif books[counter].available == "No":
                messagebox.showerror("Error", f"{borrow_val} is unavailable")
                
            found = True
            
        counter += 1

    if found == False:
        messagebox.showerror("Error", f"{borrow_val} cannot be found within the library")
        
    load()

def return_():
    """
    Displays input box to get book to be returned
    """

    clear(input_frame)

    return_var = StringVar()

    label = Label(input_frame, text="Return: ")
    entry = Entry(input_frame, textvariable=return_var)
    submit_button= Button(input_frame, text="Submit", command=lambda: return_submit(return_var))
        
    label.pack()
    entry.pack()
    submit_button.pack() 

def return_submit(var):
    """
    Changes books availbility if book is unavailable
    """
    return_val = var.get()
    found = False
    counter = 0
    
    # Loops through every item unless book is found
    while found == False and counter < len(books):
        
        if books[counter].title == return_val:
            
            if books[counter].available == "No":
                messagebox.showinfo("Library Updated", f"{return_val} is returned")
                books[counter].available = "Yes"
                
            elif books[counter].available == "Yes":
                messagebox.showerror("Error", f"{return_val} is still available and therefore cannot be \"returned\"")
            
            found = True
            
        counter += 1
    
    if found == False:
        messagebox.showerror("Error", f"{return_val} cannot be found within the library")
    
    load()

def load():
    """
    Displays list of books in table format
    """

    clear(main_frame)

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

def clear(frame):
    # Deletes every widget in the frame
    for widget in frame.winfo_children():
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

# Main program

button_info = {
    "sort": sort,
    "search": search,
    "borrow": borrow,
    "return": return_,
    "load": load,
    "save": save
}

books = csv_to_array("book.csv")  
library = Library(books) # Creates library
library.main_window = create_window(library) # Creates main window of that library

button_frame = Frame(library.main_window)
main_frame = Frame(library.main_window) 
input_frame = Frame(library.main_window)

library.main_window = create_buttons(library.main_window, button_info)

button_frame.pack()
main_frame.pack()
input_frame.pack()

library.open_() # Displays main window

