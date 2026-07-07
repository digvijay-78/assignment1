print("*" * 40)
print("     WELCOME TO MP TOUR GUIDE")
print("*" * 40)

print("\nChoose Your Destination")
print("1. Indore")
print("2. Bhopal")
print("3. Dhar")
print("4. Ujjain")

location = int(input("Enter your destination: "))

budget = int(input("\nBudget (1: Under 5000, 2: Above 5000): "))

room = input("Need room (yes/no): ").lower()

days = int(input("Days (1-3): "))

print("\nTransport")
print("1. Bus")
print("2. Train")
print("3. Bike")
print("4. Car")

transport = int(input("Enter transport: "))

# =========================
# BASE COST ESTIMATION
# =========================

food = 0
travel = 0
stay = 0

if budget == 1:
    food = 400 * days
    stay = 1000 * days
else:
    food = 800 * days
    stay = 2500 * days

if room == "no":
    stay = 0

if transport == 1:
    travel = 300 * days
elif transport == 2:
    travel = 500 * days
elif transport == 3:
    travel = 700 * days
else:
    travel = 1200 * days

total = food + stay + travel

print("\n===================================")
print("         TOUR PLAN OUTPUT")
print("===================================")

# =========================
# CITY SELECTION (MATCH CASE)
# =========================

match location:

    # ================= INDORE =================
    case 1:
        print("\nINDORE TOUR")

        if days == 1:
            print("Rajwada, Lal Bagh, Sarafa Bazaar")

        elif days == 2:
            print("Rajwada, Patalpani, Tincha Falls")

        else:
            print("Indore + Ujjain Trip (Mahakaleshwar)")

    # ================= BHOPAL =================
    case 2:
        print("\nBHOPAL TOUR")

        if days == 1:
            print("Upper Lake, Van Vihar")

        elif days == 2:
            print("Sanchi, Bhimbetka")

        else:
            print("Bhopal + Ujjain Tour")

    # ================= DHAR =================
    case 3:
        print("\nDHAR TOUR")

        if days == 1:
            print("Dhar Fort, Bhoj Shala")

        elif days == 2:
            print("Mandu Visit")

        else:
            print("Dhar + Indore + Ujjain")

    # ================= UJJAIN =================
    case 4:
        print("\nUJJAIN TOUR")

        if days == 1:
            print("Mahakaleshwar Temple, Ram Ghat")

        elif days == 2:
            print("Kal Bhairav, Sandipani Ashram")

        else:
            print("Ujjain + Indore + Bhopal")

    case _:
        print("Invalid location")

# =========================
# COST OUTPUT
# =========================

print("\nEstimated Cost Breakdown")
print("Food Cost:", food)
print("Stay Cost:", stay)
print("Travel Cost:", travel)

print("\nTOTAL ESTIMATED COST:", total)

print("\n===================================")
print("THANK YOU FOR USING MP TOUR GUIDE")
print("HAVE A SAFE JOURNEY!")
print("===================================")