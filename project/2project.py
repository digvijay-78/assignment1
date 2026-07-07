# ==============================
# INDORE TOURIST GUIDE
# ==============================

print("\nChoose Budget")
print("1. Under ₹5000")
print("2. ₹5000 OR ABOVE")
budget = int(input("Enter your choice: "))

print("\nWant room or not?")
room = input("yes/no: ").lower()

print("\nHow many days will you stay?")
days = int(input("Enter number of days (1-3): "))

print("\nChoose Transport")
print("1. Bus")
print("2. Train")
print("3. Bike")
print("4. Car")
transport = int(input("Enter your choice: "))

print("\n===================================")
print("        INDORE TOUR PLAN")
print("===================================")

# =========================
# BUDGET 1
# =========================

if budget == 1:

    # ---------------- ROOM YES ----------------
    if room == "yes":

        # BUS
        if transport == 1:

            if days == 1:
                print("\n1 DAY TRIP")
                print("Rajwada Palace")
                print("Lal Bagh Palace")
                print("Kanch Mandir")
                print("Sarafa Bazaar")
                print("Room Required")
                print("Food: ₹300 - ₹500")
                print("Transport: ₹200 - ₹400")

            elif days == 2:
                print("\n2 DAY TRIP")
                print("Day 1: Rajwada, Lal Bagh, Kanch Mandir")
                print("Day 2: Patalpani Waterfall, Tincha Falls, Chappan Dukan")
                print("Room Required")
                print("Food: ₹600 - ₹800")
                print("Transport: ₹400 - ₹700")

            else:
                print("\n3 DAY TRIP")
                print("Day 1: Rajwada, Lal Bagh, Sarafa Bazaar")
                print("Day 2: Patalpani, Ralamandal Sanctuary")
                print("Day 3: Ujjain - Mahakaleshwar Temple, Ram Ghat")
                print("Room Required")
                print("Food: ₹900 - ₹1200")
                print("Transport: ₹800 - ₹1200")

        # TRAIN
        elif transport == 2:

            if days == 1:
                print("\n1 DAY TRIP")
                print("Rajwada Palace")
                print("Sarafa Bazaar")
                print("Kanch Mandir")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY TRIP")
                print("Rajwada + Lal Bagh + Patalpani")
                print("Room Required")

            else:
                print("\n3 DAY TRIP")
                print("Indore + Ujjain Trip")
                print("Mahakaleshwar Temple Visit")
                print("Room Required")

        # BIKE
        elif transport == 3:

            if days == 1:
                print("\n1 DAY BIKE TRIP")
                print("Rajwada")
                print("Sarafa Bazaar")
                print("Kanch Mandir")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY BIKE TRIP")
                print("Patalpani + Tincha Falls")
                print("Room Required")

            else:
                print("\n3 DAY BIKE TRIP")
                print("Indore + Ujjain Full Trip")
                print("Room Required")

        # CAR
        else:

            if days == 1:
                print("\n1 DAY CAR TRIP")
                print("Rajwada + Lal Bagh + Sarafa")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY CAR TRIP")
                print("Indore Full Tour")
                print("Waterfalls Visit")
                print("Room Required")

            else:
                print("\n3 DAY CAR TRIP")
                print("Indore + Ujjain Complete Tour")
                print("Room Required")

    # ---------------- ROOM NO ----------------
    else:

        if transport == 1:

            if days == 1:
                print("\n1 DAY TRIP")
                print("Rajwada")
                print("Sarafa Bazaar")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRIP")
                print("Rajwada + Patalpani")
                print("No Room")

            else:
                print("\n3 DAY TRIP")
                print("Indore + Ujjain Trip")
                print("No Room")

        elif transport == 2:

            if days == 1:
                print("\n1 DAY TRIP")
                print("Rajwada + Sarafa")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRIP")
                print("Indore Sightseeing")
                print("No Room")

            else:
                print("\n3 DAY TRIP")
                print("Indore + Ujjain")
                print("No Room")

        elif transport == 3:

            print("\nBIKE TRIP")
            print("Indore Local Travel")
            print("No Room")

        else:

            print("\nCAR TRIP")
            print("Indore + Nearby Places")
            print("No Room")

# =========================
# BUDGET 2
# =========================

else:

    if room == "yes":
        print("\nPREMIUM TRIP - INDORE")
        print("Luxury Hotel Included")
    else:
        print("\nSTANDARD TRIP - INDORE")
        print("No Room Required")

    if days == 1:
        print("1 Day Premium Tour")
    elif days == 2:
        print("2 Day Premium Tour")
    else:
        print("3 Day Premium Indore + Ujjain Tour")



# ==============================
# BHOPAL TOURIST GUIDE
# ==============================

print("\n===================================")
print("        BHOPAL TOUR PLAN")
print("===================================")

if budget == 1:

    # ---------------- ROOM YES ----------------
    if room == "yes":

        if transport == 1:   # BUS

            if days == 1:
                print("\n1 DAY TRIP - BHOPAL")
                print("Upper Lake")
                print("Van Vihar National Park")
                print("Bharat Bhavan")
                print("New Market")
                print("Room Required")
                print("Food: ₹300 - ₹500")
                print("Transport: ₹200 - ₹400")

            elif days == 2:
                print("\n2 DAY TRIP - BHOPAL")
                print("Day 1: Upper Lake, Van Vihar, Bharat Bhavan")
                print("Day 2: Sanchi Stupa, Bhimbetka Caves")
                print("Room Required")
                print("Food: ₹600 - ₹900")
                print("Transport: ₹400 - ₹700")

            else:
                print("\n3 DAY TRIP - BHOPAL + NEARBY")
                print("Day 1: Upper Lake, New Market")
                print("Day 2: Sanchi + Bhimbetka")
                print("Day 3: Bhojpur Temple, Kerwa Dam")
                print("Room Required")
                print("Food: ₹900 - ₹1200")
                print("Transport: ₹800 - ₹1200")

        elif transport == 2:   # TRAIN

            if days == 1:
                print("\n1 DAY TRIP - BHOPAL")
                print("Upper Lake")
                print("Van Vihar")
                print("New Market")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY TRIP - BHOPAL")
                print("Upper Lake + Museum + Sanchi")
                print("Room Required")

            else:
                print("\n3 DAY TRIP - BHOPAL + UJJAIN")
                print("Bhopal Sightseeing")
                print("Sanchi Stupa")
                print("Ujjain - Mahakaleshwar Temple")
                print("Room Required")

        elif transport == 3:   # BIKE

            if days == 1:
                print("\n1 DAY BIKE TRIP - BHOPAL")
                print("Upper Lake")
                print("Van Vihar")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY BIKE TRIP")
                print("Bhopal + Sanchi Visit")
                print("Room Required")

            else:
                print("\n3 DAY BIKE TRIP")
                print("Bhopal + Bhimbetka + Ujjain")
                print("Room Required")

        else:  # CAR

            if days == 1:
                print("\n1 DAY CAR TRIP - BHOPAL")
                print("Upper Lake + Bharat Bhavan")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY CAR TRIP")
                print("Bhopal Full Tour")
                print("Sanchi Stupa Visit")
                print("Room Required")

            else:
                print("\n3 DAY CAR TRIP")
                print("Bhopal + Ujjain Luxury Trip")
                print("Room Required")

    # ---------------- ROOM NO ----------------
    else:

        if transport == 1:

            if days == 1:
                print("\n1 DAY TRIP - BHOPAL")
                print("Upper Lake")
                print("Van Vihar")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRIP - BHOPAL")
                print("Bhopal Sightseeing")
                print("Sanchi Visit")
                print("No Room")

            else:
                print("\n3 DAY TRIP - BHOPAL + UJJAIN")
                print("Bhopal + Sanchi + Ujjain")
                print("No Room")

        elif transport == 2:

            if days == 1:
                print("\n1 DAY TRAIN TRIP")
                print("Upper Lake + New Market")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRAIN TRIP")
                print("Bhopal + Museum + Sanchi")
                print("No Room")

            else:
                print("\n3 DAY TRAIN TRIP")
                print("Bhopal + Ujjain Trip")
                print("No Room")

        elif transport == 3:

            print("\nBIKE TRIP - BHOPAL")
            print("Local Sightseeing")
            print("No Room")

        else:

            print("\nCAR TRIP - BHOPAL")
            print("Bhopal + Nearby Places")
            print("No Room")

# =========================
# BUDGET 2
# =========================

else:

    if room == "yes":
        print("\nPREMIUM BHOPAL TOUR")
        print("Luxury Hotel Stay Included")
    else:
        print("\nSTANDARD BHOPAL TOUR")
        print("No Room Required")

    if days == 1:
        print("1 Day Luxury Bhopal Tour")
    elif days == 2:
        print("2 Day Luxury Bhopal Tour")
    else:
        print("3 Day Luxury Bhopal + Ujjain Tour")



# ==============================
# DHAR TOURIST GUIDE
# ==============================

print("\n===================================")
print("          DHAR TOUR PLAN")
print("===================================")

if budget == 1:

    # ---------------- ROOM YES ----------------
    if room == "yes":

        if transport == 1:   # BUS

            if days == 1:
                print("\n1 DAY TRIP - DHAR")
                print("Dhar Fort")
                print("Bhoj Shala")
                print("Jheera Bagh Palace")
                print("Room Required")
                print("Food: ₹300 - ₹500")
                print("Transport: ₹200 - ₹400")

            elif days == 2:
                print("\n2 DAY TRIP - DHAR")
                print("Day 1: Dhar Fort, Bhoj Shala")
                print("Day 2: Mandu Visit")
                print("Jahaz Mahal, Hindola Mahal")
                print("Room Required")
                print("Food: ₹600 - ₹900")
                print("Transport: ₹400 - ₹700")

            else:
                print("\n3 DAY TRIP - DHAR + NEARBY")
                print("Day 1: Dhar Fort, Bhoj Shala")
                print("Day 2: Mandu Full Tour")
                print("Day 3: Indore or Omkareshwar Visit")
                print("Room Required")
                print("Food: ₹900 - ₹1200")
                print("Transport: ₹800 - ₹1200")

        elif transport == 2:   # TRAIN

            if days == 1:
                print("\n1 DAY TRIP - DHAR")
                print("Dhar Fort")
                print("Bhoj Shala")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY TRIP - DHAR")
                print("Dhar + Mandu Visit")
                print("Room Required")

            else:
                print("\n3 DAY TRIP - DHAR + UJJAIN")
                print("Dhar + Mandu + Ujjain Trip")
                print("Room Required")

        elif transport == 3:   # BIKE

            if days == 1:
                print("\n1 DAY BIKE TRIP - DHAR")
                print("Dhar Fort + Bhoj Shala")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY BIKE TRIP")
                print("Dhar + Mandu Ride")
                print("Room Required")

            else:
                print("\n3 DAY BIKE TRIP")
                print("Dhar + Mandu + Indore/Ujjain")
                print("Room Required")

        else:  # CAR

            if days == 1:
                print("\n1 DAY CAR TRIP - DHAR")
                print("Dhar Fort + Jheera Bagh")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY CAR TRIP")
                print("Dhar + Mandu Full Tour")
                print("Room Required")

            else:
                print("\n3 DAY CAR TRIP")
                print("Dhar + Mandu + Nearby Cities")
                print("Room Required")

    # ---------------- ROOM NO ----------------
    else:

        if transport == 1:

            if days == 1:
                print("\n1 DAY TRIP - DHAR")
                print("Dhar Fort")
                print("Bhoj Shala")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRIP - DHAR")
                print("Dhar + Mandu Visit")
                print("No Room")

            else:
                print("\n3 DAY TRIP - DHAR + NEARBY")
                print("Dhar + Mandu + Indore")
                print("No Room")

        elif transport == 2:

            if days == 1:
                print("\n1 DAY TRAIN TRIP")
                print("Dhar Fort Visit")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRAIN TRIP")
                print("Dhar + Mandu")
                print("No Room")

            else:
                print("\n3 DAY TRAIN TRIP")
                print("Dhar + Ujjain Trip")
                print("No Room")

        elif transport == 3:

            print("\nBIKE TRIP - DHAR")
            print("Local Dhar Tour")
            print("No Room")

        else:

            print("\nCAR TRIP - DHAR")
            print("Dhar + Nearby Places")
            print("No Room")

# =========================
# BUDGET 2
# =========================

else:

    if room == "yes":
        print("\nPREMIUM DHAR TOUR")
        print("Luxury Stay Included")
    else:
        print("\nSTANDARD DHAR TOUR")
        print("No Room Required")

    if days == 1:
        print("1 Day Dhar Luxury Tour")
    elif days == 2:
        print("2 Day Dhar + Mandu Tour")
    else:
        print("3 Day Dhar Full MP Tour")

print("\n===================================")
print("THANK YOU FOR USING MP TOUR GUIDE")




# ==============================
# UJJAIN TOURIST GUIDE
# ==============================

print("\n===================================")
print("         UJJAIN TOUR PLAN")
print("===================================")

if budget == 1:

    # ---------------- ROOM YES ----------------
    if room == "yes":

        if transport == 1:   # BUS

            if days == 1:
                print("\n1 DAY TRIP - UJJAIN")
                print("Mahakaleshwar Temple")
                print("Ram Ghat")
                print("Harsiddhi Temple")
                print("Room Required")
                print("Food: ₹300 - ₹500")
                print("Transport: ₹200 - ₹400")

            elif days == 2:
                print("\n2 DAY TRIP - UJJAIN")
                print("Day 1: Mahakaleshwar, Ram Ghat")
                print("Day 2: Kal Bhairav, Sandipani Ashram")
                print("Room Required")
                print("Food: ₹600 - ₹900")
                print("Transport: ₹400 - ₹700")

            else:
                print("\n3 DAY TRIP - UJJAIN + NEARBY")
                print("Day 1: Mahakaleshwar Temple")
                print("Day 2: Kal Bhairav + Mangalnath")
                print("Day 3: Indore Visit")
                print("Room Required")
                print("Food: ₹900 - ₹1200")
                print("Transport: ₹800 - ₹1200")

        elif transport == 2:   # TRAIN

            if days == 1:
                print("\n1 DAY TRIP - UJJAIN")
                print("Mahakaleshwar Temple")
                print("Ram Ghat")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY TRIP - UJJAIN")
                print("Mahakaleshwar + Kal Bhairav")
                print("Room Required")

            else:
                print("\n3 DAY TRIP - UJJAIN + BHOPAL")
                print("Ujjain + Bhopal Full Trip")
                print("Room Required")

        elif transport == 3:   # BIKE

            if days == 1:
                print("\n1 DAY BIKE TRIP - UJJAIN")
                print("Mahakaleshwar Temple")
                print("Ram Ghat")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY BIKE TRIP")
                print("Ujjain + Kal Bhairav")
                print("Room Required")

            else:
                print("\n3 DAY BIKE TRIP")
                print("Ujjain + Indore + Bhopal")
                print("Room Required")

        else:  # CAR

            if days == 1:
                print("\n1 DAY CAR TRIP - UJJAIN")
                print("Mahakaleshwar + Ram Ghat")
                print("Room Required")

            elif days == 2:
                print("\n2 DAY CAR TRIP")
                print("Ujjain Full Tour")
                print("Room Required")

            else:
                print("\n3 DAY CAR TRIP")
                print("Ujjain + MP Full Tour")
                print("Room Required")

    # ---------------- ROOM NO ----------------
    else:

        if transport == 1:

            if days == 1:
                print("\n1 DAY TRIP - UJJAIN")
                print("Mahakaleshwar Temple")
                print("Ram Ghat")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRIP - UJJAIN")
                print("Mahakaleshwar + Kal Bhairav")
                print("No Room")

            else:
                print("\n3 DAY TRIP - UJJAIN + NEARBY")
                print("Ujjain + Indore Visit")
                print("No Room")

        elif transport == 2:

            if days == 1:
                print("\n1 DAY TRAIN TRIP")
                print("Mahakaleshwar Temple")
                print("No Room")

            elif days == 2:
                print("\n2 DAY TRAIN TRIP")
                print("Ujjain Sightseeing")
                print("No Room")

            else:
                print("\n3 DAY TRAIN TRIP")
                print("Ujjain + Bhopal Trip")
                print("No Room")

        elif transport == 3:

            print("\nBIKE TRIP - UJJAIN")
            print("Local Temple Visit")
            print("No Room")

        else:

            print("\nCAR TRIP - UJJAIN")
            print("Ujjain + Nearby Places")
            print("No Room")

# =========================
# BUDGET 2
# =========================

else:

    if room == "yes":
        print("\nPREMIUM UJJAIN TOUR")
        print("Luxury Hotel Stay Included")
    else:
        print("\nSTANDARD UJJAIN TOUR")
        print("No Room Required")

    if days == 1:
        print("1 Day Ujjain Luxury Tour")
    elif days == 2:
        print("2 Day Ujjain Premium Tour")
    else:
        print("3 Day Ujjain + MP Luxury Tour")

# =========================
# INVALID INPUT HANDLING
# =========================

if budget != 1 and budget != 2:
    print("\nInvalid Budget Input")

if room != "yes" and room != "no":
    print("\nInvalid Room Input")

if transport < 1 or transport > 4:
    print("\nInvalid Transport Input")

if days < 1 or days > 3:
    print("\nInvalid Days Input")

# =========================
# END MESSAGE
# =========================

print("\n===================================")
print("THANK YOU FOR USING MP TOUR GUIDE")
print("HAVE A SAFE JOURNEY!")
print("===================================")