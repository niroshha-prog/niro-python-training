from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def _init_(self, item_id, name):
        self.item_id = item_id
        self.name = name
        self.is_issued = False

    @abstractmethod
    def issue(self):
        pass

    def return_item(self):
        if self.is_issued:
            self.is_issued = False
            print(f"{self.name} returned successfully")
        else:
            print("Item was not issued")


class Book(LibraryItem):

    def _init_(self, item_id, name, author):
        super()._init_(item_id, name)
        self.author = author

    def issue(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"Book '{self.name}' by {self.author} issued for 14 days")
        else:
            print("Book already issued")


# Main Program
book1 = Book(101, "Python Basics", "John Smith")

print("Book ID:", book1.item_id)
print("Book Name:", book1.name)
print("Author:", book1.author)

book1.issue()
book1.return_item()