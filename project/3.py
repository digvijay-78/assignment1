print("*"*40)
print("     WELCOME TO MP TOUR GUIDE")
print("*"*40)

print("""Choose Your Destination
1- Indore
2- Bhopal
3- Dhar
4- Ujjain""")

location=int(input("Enter your destination:"))

print('''Travel Options
1- below rs5000
2- above rs5000''')
budgt=int(input("Enter =:"))
room,day=input("room(yes/no),day(1-3), sep by ',' :").split(",")
print("""Transport Options
1- Bus
2- Train
3- Bike
4- Car""")
trans=int(input("Enter transport:"))
budgt=int(budgt)
day=int(day)
trans=int(trans)
room=room.lower()

food=0
travel=0
stay=0

if budgt==1:
    food=500*day
    stay=1000*day
else:
    food=800*day
    stay=2000*day

if room=="no":
    stay=0

match trans:
    case 1:
        travel=300*day
    case 2:
        travel=500*day
    case 3:
        travel=700*day
    case _:
        travel=1200*day

total=food+stay+travel

print("="*40)
print("TOUR PLAN")
print("="*40)

match location:
    case 1:
        print("INDORE TOUR")

        if day==1:
            print("Day 1:")
            print("- rajwada palace")
            print("- lal bagh palace")
            print("- sarafa Night Market")
        elif day==2:
            print("Day 1:")
            print("- rajwada palace")
            print("- lal bagh palace")
            print("- khajrana ganesh temple")
            print("- sarafa Night Market")
            print("Day 2:")
            print("- Patalpani waterfall")
            print("- Tincha falls")
            print("- Choral Dam")
            print("- 56 Dukan ")
        else:
            print("Day 1:")
            print("- rajwada palace")
            print("- lal bagh palace")
            print("- khajrana ganesh temple")
            print("Day 2:")
            print("- Patalpani waterfall")
            print("- Tincha falls")
            print("- Janapav Kuti")
            print("Day 3:")
            print("- Mahakaleshwar Temple (Ujjain)")
            print("- Ram Ghat")
            print("- Kal Bhairav temple")

        print("must try food:")
        print("- poha")
        print("- jalebi")
        print("- bhutte Ka Kees")
        print("souvenir (the things you can take as a memento or keepsake )suggestions")
        print("- indori Namkeen")
        print("- ratlami Sev")
        print("- cotton Handloom Products")

    case 2:
        print("BHOPAL TOUR")

        if day==1:
            print("Day 1:")
            print("-  upper lake")
            print("- Van vihar national park")
            print("- Birla Museum")
            print("- Boat Club")
            print("- tribal museum")
        elif day==2:
            print("Day 1:")
            print("-  upper lake")
            print("- Van vihar national park")
            print("- Boat Club")
            print("- Birla Temple")
            print("Day 2:")
            print("- Sanchi Stupa")
            print("- Bhimbetka Rock Shelters")
            print("- Udayagiri Caves")
        else:
            print("Day 1:")
            print("-  upper lake")
            print("- Van vihar national park")
            print("- tribal museum")
            print("Day 2:")
            print("- Sanchi Stupa")
            print("- Bhimbetka Rock Shelters")
            print("- Bhojpur Shiva Temple")
            print("Day 3:")
            print("- Udayagiri Caves")
            print("- Kerwa Dam")
            print("- Manuabhan Tekri")

        print("souvenir (the things you can take as a memento or keepsake )suggestions")
        print("- Zardozi Embroidery")
        print("- Tribal Handicrafts")
        print("- Bhopali Batua ")

    case 3:
        print("DHAR TOUR")

        if day==1:
            print("Day 1:")
            print("- Dhar Fort")
            print("- Bhoj Shala")
            print("- Kharbuja Mahal")
            print("- Jheera Bagh palace")
            print("- Lath Masjid")
        elif day==2:
            print("Day 1:")
            print("- Dhar Fort")
            print("- Bhoj Shala")
            print("- Kharbuja Mahal")
            print("Day 2:")
            print("- Mandu Fort")
            print("- Jahaz Mahal")
            print("- Hindola Mahal")
            print("- Rani Roopmati Pavilion")
            print("- Baz Bahadur palace")
        else:
            print("Day 1:")
            print("- Dhar Fort")
            print("- Bhoj Shala")
            print("- Jheera Bagh palace")
            print("Day 2:")
            print("- Mandu Fort")
            print("- Jahaz Mahal")
            print("- Hindola Mahal")
            print("- Rani Roopmati Pavilion")
            print("Day 3:")
            print("- Baz Bahadur palace")
            print("- Rewa Kund")
            print("- Nilkanth Mahadev Temple")

        print("souvenir (the things you can take as a memento or keepsake )suggestions")
        print("- Maheshwari Sarees")
        print("- Wooden Handicrafts")
        print("- Tribal Artifacts")

    case 4:
        print("UJJAIN TOUR")

        if day==1:
            print("Day 1:")
            print("- Mahakaleshwar Jyotirlinga Temple")
            print("- Ram Ghat")
            print("- Harsiddhi Temple")
            print("- Bade Ganeshji Ka Mandir")
            print("- Mahakal Corridor")
        elif day==2:
            print("Day 1:")
            print("- Mahakaleshwar Jyotirlinga Temple")
            print("- Ram Ghat")
            print("- Harsiddhi Temple")
            print("Day 2:")
            print("- Kal Bhairav Temple")
            print("- Sandipani Ashram")
            print("- ISKCON Temple")
            print("- Mangalnath Temple")
            print("- Chintaman Ganesh Temple")
        else:
            print("Day 1:")
            print("- Mahakaleshwar Jyotirlinga Temple")
            print("- Ram Ghat")
            print("- Harsiddhi Temple")
            print("Day 2:")
            print("- Kal Bhairav Temple")
            print("- Sandipani Ashram")
            print("- Mangalnath Temple")
            print("- Chintaman Ganesh Temple")
            print("Day 3:")
            print("- ISKCON Temple")
            print("- Bhartrihari Caves")
            print("- Gopal Mandir")
            print("- Gadkalika Temple")
            print("- Kaliadeh palace")

        print("souvenir (the things you can take as a memento or keepsake )suggestions")
        print("- Rudraksha Mala")
        print("- Religious Idols")
        print("- Incense Sticks")

    case _:
        print("invalid ")

print("estimated cost breakdown")
print("Food Cost={}\nStay Cost={}\nTravel Cost={}".format(food,stay,travel))

print("TOTAL ESTIMATED COST:",total)
rating=int(input("Rate our service (1-5): "))
print("Thank you for your feedback!")

print("""emergency contacts
Police      : 100
Ambulance   : 108
Fire        : 101
Tourist Help: 1363""")

print("="*40)
print("THANK YOU FOR USING MP TOUR GUIDE")
print("HAVE A SAFE JOURNEY!")
print("="*40)