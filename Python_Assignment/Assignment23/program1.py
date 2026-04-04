class BookStore:
    NoOfBook = 0

    def __init__(self,Name,Author):
        self.BookName = Name
        self.Author = Author

        BookStore.NoOfBook += 1


    def Display(self):
        print(f" {self.BookName} by {self.Author}. No of Books : {BookStore.NoOfBook}")


bobj1 = BookStore("Linux System Programming", "Robert Love")
bobj1.Display()

bobj2 = BookStore("C Programming","Dennis Ritchie")
bobj2.Display()