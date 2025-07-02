import csv
import tkinter as tk
from tkinter import *
from tkinter import messagebox, tt

class LibraryApp:
    def __init__(self, csv_file="book.csv"):
        self.books = self.csv_to_array(csv_file)
        self.library = Library(self.books)
        self.search_pos = -1

        self.button_info = {
            "sort": self.sort,
            "search": self.search,
            "borrow": self.borrow,
            "return": self.return_,
            "load": self.load,
            "save": self.save
        }

        self.library.main_window = self.create_window()
        self.button_frame = Frame(self.library.main_window)
        self.main_frame = Frame(self.library.main_window)
        self.input_frame = Frame(self.library.main_window)

        self.create_buttons()
        self.button_frame.pack()
        self.main_frame.pack()
        self.input_frame.pack()

    def run(self):
        self.library.open()

    def create_window(self):
    
        window = Tk()
        window.geometry("1000x500")
        window.title(library.name)
    
        return window
    
    def create_buttons(self):
        """
        Returns a window with a row of buttons
        """
    
        for x, y in self.button_info.items():
            button = Button(self.button_frame, text=x, command=y)
            button.pack(side=LEFT)
        
        return window  
    
    def sort(self):
        """
        Displays input box to get value to be sorted by
        """
        self.clear(input_frame)
    
        self.library.searched = False
        sort_var = StringVar()
    
        label = Label(self.input_frame, text="Sort by:")
        entry = Entry(self.input_frame, textvariable=sort_var)
        submit_button = Button(self.input_frame, text="Submit", command=lambda: sort_submit(sort_var))
            
        label.pack()
        entry.pack()
        submit_button.pack()
        
    def sort_submit(self, var):
        """
        Displays bubble-sorted list of books by sort by value as inputted by user
        """
        sort_val = var.get()
        
        if self.validate_sort_val(sort_val):
            
            n = len(books)
    
            for i in range(n):
    
                for j in range(n-1):
    
                    if self.books[j].get(sort_val) > self.books[j+1].get(sort_val):
                        self.books[j], self.books[j+1] = self.books[j+1], self.books[j]
            load()
        
        else:
            messagebox.showerror("Error", "Input must either id, title, author, or genre")
        
    def validate_sort_val(self, sort_val):
    
        if sort_val.lower() in ["id", "title", "author", "genre"]:
    
            if sort_val.lower() == "title":
                self.library.sorted_by_title = True
    
            return True
        else:
            print(sort_val)
            return False
        
    def search(self):
        """
        Displays input box to get a value to search for
        """
    
        self.clear(input_frame)
    
        search_var = StringVar()
        
        if self.library.sorted_by_title:
            
            label = Label(self.input_frame, text="Search:")
            entry = Entry(self.input_frame, textvariable=search_var) # This gives the actual input box
            submit_button= Button(self.input_frame, text="Submit", command=lambda: search_submit(search_var))
            
            label.pack()
            entry.pack()
            submit_button.pack() 
            
        else:
            messagebox.showerror("Error", "Library must be sorted by title before search")
            
    def search_submit(self, var):
        """
        Highlights search book inputted by user through a binary search
        """
        
        search_val = var.get()
    
        low = 0
        high = len(self.books) - 1
        mid = 0
        found = False
    
        while low <= high and found == False:
            mid = (high + low) // 2
                
            # If search_var is greater, ignore left half
            if self.books[mid].title < search_val:
                low = mid + 1
    
            # If search_var is smaller, ignore right half
            elif self.books[mid].title > search_val:
                high = mid - 1
    
            # Means search_var is present at mid
            else:
                self.library.searched = True
                self.search_pos = mid
                self.load()
                found = True
                    
        if found == False:
            messagebox.showerror("Error", f"{search_val} cannot be found within library")
    
    def borrow(self):
        """
        Displays input box to get book to be borrowed
        """
    
        self.clear(input_frame)
    
        borrow_var = StringVar()
    
        label = Label(self.input_frame, text="Borrow: ")
        entry = Entry(self.input_frame, textvariable=borrow_var)
        submit_button= Button(self.input_frame, text="Submit", command=lambda: borrow_submit(borrow_var))
            
        label.pack()
        entry.pack()
        submit_button.pack() 
            
    def borrow_submit(self, var):
        """
        Changes books availbility if book is available
        """
        borrow_val = var.get()
        found = False
        counter = 0
        
        # Loops through every item unless book is found
        while found == False and counter < len(books):
            
            if self.books[counter].title == borrow_val:
    
                if self.books[counter].available == "Yes":
                    messagebox.showinfo("Library Updated", f"{borrow_val} is borrowed")
                    self.books[counter].available = "No"
                    
                elif self.books[counter].available == "No":
                    messagebox.showerror("Error", f"{borrow_val} is unavailable")
                    
                found = True
                
            counter += 1
    
        if found == False:
            messagebox.showerror("Error", f"{borrow_val} cannot be found within the library")
            
        self.load()
    
    def return_(self):
        """
        Displays input box to get book to be returned
        """
    
        self.clear(input_frame)
    
        return_var = StringVar()
    
        label = Label(self.input_frame, text="Return: ")
        entry = Entry(self.input_frame, textvariable=return_var)
        submit_button= Button(self.input_frame, text="Submit", command=lambda: return_submit(return_var))
            
        label.pack()
        entry.pack()
        submit_button.pack() 
    
    def return_submit(self, var):
        """
        Changes books availbility if book is unavailable
        """
        return_val = var.get()
        found = False
        counter = 0
        
        # Loops through every item unless book is found
        while found == False and counter < len(books):
            
            if self.books[counter].title == return_val:
                
                if selfbooks[counter].available == "No":
                    messagebox.showinfo("Library Updated", f"{return_val} is returned")
                    books[counter].available = "Yes"
                    
                elif self.books[counter].available == "Yes":
                    messagebox.showerror("Error", f"{return_val} is still available and therefore cannot be \"returned\"")
                
                found = True
                
            counter += 1
        
        if found == False:
            messagebox.showerror("Error", f"{return_val} cannot be found within the library")
        
        self.load()
    
    def load(self):
        """
        Displays list of books in table format
        """
    
        self.clear(main_frame)
    
        label = Label(self.main_frame, text="Books:")
        treeview = ttk.Treeview(
                                self.main_frame,
                                columns=("ID", "Title", "Author", "Genre","Available"),
                                show="headings"
                                )
        treeview.heading("ID", text="ID")
        treeview.heading("Title", text="Title")
        treeview.heading("Author", text="Author")
        treeview.heading("Genre", text="Genre")
        treeview.heading("Available", text="Available")
        
        items = []
        
        for book in self.books:
            item_id = treeview.insert(
                                    "",
                                    END,
                                    values=(
                                             book.ID, book.title, book.author,
                                             book.genre, book.available))
            items.append(item_id)
    
        if self.library.searched:
            book = self.books[self.search_pos]
            treeview.item(items[self.search_pos], values=(book.ID, book.title.upper(), book.author.upper(),
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
    
    def csv_to_array(self, file_name):
        
        array = []
        file = open(file_name, "r")
    
        for row in csv.reader(file):
            array.append(Book(
                                row[0],row[1],
                                row[2],row[3], row[4]
                                ))
    
        file.close()
    
        return array
    