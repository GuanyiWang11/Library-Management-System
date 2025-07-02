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