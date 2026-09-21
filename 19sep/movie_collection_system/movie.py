movies=[]

class Movie:
    def __init__(self):
        self.id=input("enter the movie id  : ").lower()
        self.name=input("enter the movie name : ")
        self.genre=input("enter the movie genre").lower()
        self.rating=float(input("enter the rating"))
        self.price=int(input("enter the ticket price"))
        movies.append(self)
    def display(self):
        print("\nMOVIES :\n")
        for i in movies:
            print(i.id,i.name,i.genre,i.rating,i.price)
    def rating_8(self):
        print("\nMovies with rating greater than 8:\n")
        for i in movies:
            if i.ratinng>=8:
                print(i.name," ",i.rating)
    def genre_action(self):
        print("\nAction Movies:\n")
        for i in movies:
            if i.genre=="action":
                print(i.name)
    def highest_rated(self):
        print("\nHighest Rated Movie:\n")
        a=movies[0]
        for i in movies:
            if i.rating>a.rating:
                a=i
        print(a.name,a.rating)
    def search(self):
        a=input("enter the id you want to search").lower()
        for i in movies:
            if i.id==a:
                print("\nmovie found:\n",i.id,i.name,i.genre,i.rating,i.price)
                return
        else:
            print("not found")
    def avg(self):
        print("Average Movie Rating:" )
        a=0
        c=0
        for i in movies:
            a+=i.rating
            c+=1
        avg_rating=a/c
        print(avg_rating)
    def greater_300(self):
        print("Movies with ticket price greater than 300:")
        for i in movies:
            if i.price>300:
                print(i.name,i.price)
