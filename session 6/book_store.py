# Question 2,3,4,5

import csv

class  Book(object):
    
    # Question 2 code
    def __init__(self, book_id, title, author, binding, pages,  price, isbn, image_url):
        """
        Letter object takes 8 arguments
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.binding = binding
        self.pages = pages
        self.price = price
        self.isbn = isbn
        self.image_url = image_url

    def __str__(self):
        print("\nbook_id: {}\nTitle: {}\nAuthor: {}\nBinding: {}\nPages: {}\nPrice: {}\nIsbn: {}\nImage_url: {}".format(self.book_id, self.title, self.author, self.binding, 
        self.pages, self.price,  self.isbn, self.image_url))

class EBook(Book):
    def __init__(self, book_id, title, author, binding, pages,  price, isbn, image_url, book_format, size_in_kb, is_drm_protected):
        self.book_format = book_format
        self.size_in_kb = size_in_kb
        self.is_drm_protected = is_drm_protected
        super().__init__(book_id, title, author, binding, pages,  price, isbn, image_url)

    def __str__(self):
        print("\nbook_id: {}\nTitle: {}\nAuthor: {}\nBinding: {}\nPages: {}\nPrice: {}\nIsbn: {}\nImage_url: {}\nFormat: {}\nSize_in_kb: {}\nIs_drm_protected: {}".format(self.book_id, self.title, self.author, self.binding, 
        self.pages, self.price,  self.isbn, self.image_url, self.book_format, self.size_in_kb, self.is_drm_protected))
        
current_book = []
with open('100books.csv') as csv_file:
    books = csv.DictReader(csv_file)
    print("\nBook titles from 100books.csv file\n")
    iteration = 1
    for book in books:
        print("{}. {}".format(iteration, book['title'])) # Question 3 code
        iteration = iteration + 1
        current_book.append(Book(book['book_id'], book['title'], book['author'], book['binding'], book['pages'], book['price'], book['isbn'], book['image_url']))
    print("\nBOOK DETAILS\n") # Question 4 code
    for cur_book in current_book :
        cur_book.__str__()

# Question 5 code
print("\n\nEBOOK Details")
ebook = EBook("PARZHDA0F3NTQF3A69F5L4OHWUQ2DI", "rupal 6 Site Builder Solutions", "Mark Noble", "PB", "356", "375", "9788184046755", "http://bcbdatamedia.s3.amazonaws.com/productMedia/image_thumbs/0ba772d4-cfb9-4cf5-93b8-3f289d52e929_zlgozz7xq819mxh__256.jpg", "pdf", "150","Yes")
ebook.__str__()

ebook = EBook("PARZHDA0F33CNZ4SPGXXZTHHCGC58B", "Mastering OpenCV with Practical Computer Vision Projects", "David Millan Escriva", "PB", "352", "600", "9789351100973", "http://bcbdatamedia.s3.amazonaws.com/productMedia/image_thumbs/0b8f0e16-b0b4-49fe-b416-e08f5313a183_060agws48fvl25b__256.jpg", "word document", "150","NO")
ebook.__str__()