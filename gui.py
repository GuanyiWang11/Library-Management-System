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
    
    