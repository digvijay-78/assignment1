books=[]
class Book:
    def __init__(self):
        self.id=input("enter the book id").lower()
        self.name=input("enter the book name")
        self.author=input("enter the author name").lower()
        self.price=float(input("enter the book price"))
        books.append(self)
    def display(self):
        print("\nAll Books:\n")
        for i in books:
            print(i.id,i.name,i.author,i.price,"\n")
    def search(self):
        self.search_book=input("enter the book id you want to search").lower()
        for i in books:
            if i.id==self.search_book:
                print("books found\n",i.id,i.name,i.author,i.price)
                return
        print("book not found")
    def particular_writter(self):
        print("finding the books")
        self.particular=input("enter the author name").lower()
        for i in books:
            if i.author==self.particular:
                print(i.id,i.name,i.author,i.price)
            else: 
                print("not found")
    def greater_500(self):
        print("Books with price greater than 500:")
        for i in books:
            if i.price>500:
                print(i.id,i.name,i.author,i.price)
            else:        
                print("enter not found")

    def expensive(self):
        m=books[0]
        for i in books:
            if i.price>m.price:
                m=i
        print("Most Expensive Book:\n",m.name,"=",m.price)
    def avg(self):
        c=0
        m=0
        for i in books:
            c+=i.price
            m+=1
        avg_book=c/m
        print("Average Price:\n",avg_book)