# from rich import print

# print("[bold red]Hello[/bold red]")
# print("[green]Python[/green]")

# from rich import print

# print("[red]Hello[/red]")
# print("[green]Success[/green]")
# print("[bold]Python[/bold]")

# from rich.console import Console

# c = Console()

# c.print("Hello Python")
# c.print("Success", style="green")
# c.print("Error", style="red")


# from rich.table import Table
# from rich.console import Console

# c = Console()

# table = Table()

# table.add_column("Name")
# table.add_column("Age")
# table.add_column("City")

# table.add_row("Rahul", "20", "Indore")
# table.add_row("Aman", "21", "Bhopal")

# c.print(table)

# from rich.console import Console
# from rich.panel import Panel

# c = Console()

# c.print(Panel("Welcome to Hospital Management System"))

# from rich.console import Console
# from rich.table import Table
# c=Console()
# c.print("Hospital Management System",style="bold")
# c.print("Patient added successfully",style="green")
# c.print("Invalid patient",style="red")

# t=Table()
# t.add_column("Patient ID")
# t.add_column("name")
# t.add_column("age")

# t.add_row("101","aman","21")
# t.add_row("102","am","19")
# c.print(t)


# import tkinter as tk

# root = tk.Tk()

# root.title("My App")
# root.geometry("400x300")

# label = tk.Label(root, text="Hello Python")
# label.pack()

# button = tk.Button(root, text="Add Patient")
# button.pack()
# root.mainloop()


# import tkinter as tk
# root = tk.Tk()

# root.title("Hospital Management")
# root.geometry("500x400")

# name_entry = tk.Entry(root)
# name_entry.pack()

# age_entry = tk.Entry(root)
# age_entry.pack()

# def add():
#     name = name_entry.get()
#     age=age_entry.get()
#     print(name)
#     print(age)

# button = tk.Button(root, text="Add Patient", command=add)
# button.pack()
# root.mainloop()


# import winsound

# winsound.Beep(1000, 500)

# import winsound

# winsound.MessageBeep()


# import winsound

# winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
# import cv2

# img = cv2.imread(r"D:\infobeans\13sep\xys.jpg")

# print(img)

# import cv2

# img = cv2.imread(r"D:\infobeans\13sep\xys.jpg")

# print(img.shape)

# new_img = cv2.resize(img, (1000, 500))

# cv2.imshow("xys", new_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import socket

# hostname = socket.gethostname()

# ip = socket.gethostbyname(hostname)

# print(ip)


# import socket

# ip = socket.gethostbyname("google.com")

# print(ip)

# from urllib.parse import urlparse

# url = "https://www.example.com/products?id=101"

# result = urlparse(url)

# print(result)
# print(result.scheme)
# print(result.netloc)
# print(result.path)
# print(result.query)


# from urllib.parse import urlunparse

# url = urlunparse((
#     "https",
#     "www.example.com",
#     "/products",
#     "",
#     "id=101",
#     ""
# ))

# print(url)

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("My Game")

# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()



# from reportlab.pdfgen import canvas

# pdf = canvas.Canvas("report.pdf")

# pdf.drawString(100, 750, "Hospital Management System")
# pdf.drawString(100, 700, "Patient Name: Aman")
# pdf.drawString(100, 650, "Age: 21")

# pdf.save()

# from reportlab.pdfgen import canvas
# from reportlab.platypus import Table
# from reportlab.lib import colors

# pdf = canvas.Canvas("patient_report.pdf")

# # 1. Font
# pdf.setFont("Helvetica-Bold", 18)
# pdf.drawString(100, 780, "Hospital Patient Report")

# # 2. Patient information
# pdf.setFont("Helvetica", 12)
# pdf.drawString(100, 740, "Patient Name: Aman")
# pdf.drawString(100, 720, "Age: 21")
# pdf.drawString(100, 700, "Patient ID: 101")

# # 3. Line
# pdf.line(100, 680, 500, 680)

# # 4. Rectangle
# pdf.rect(90, 550, 430, 100)

# # 5. Table
# data = [
#     ["Test", "Result", "Status"],
#     ["Blood Pressure", "120/80", "Normal"],
#     ["Temperature", "98.6 F", "Normal"],
#     ["Heart Rate", "72 bpm", "Normal"]
# ]

# table = Table(data, colWidths=[150, 130, 100])

# table.wrapOn(pdf, 400, 200)
# table.drawOn(pdf, 120, 400)

# # 6. Image
# pdf.drawImage(
#     "xys.jpg",
#     100,
#     150,
#     width=150,
#     height=100
# )

# # 7. New page
# pdf.showPage()

# pdf.setFont("Helvetica-Bold", 18)
# pdf.drawString(100, 780, "Patient Report - Page 2")

# pdf.setFont("Helvetica", 12)
# pdf.drawString(100, 740, "Doctor's Notes:")
# pdf.drawString(100, 710, "Patient is healthy and requires regular checkup.")

# # 8. Save PDF
# pdf.save()




# import customtkinter as ctk

# root = ctk.CTk()

# root.title("Hospital Management")
# root.geometry("500x400")

# root.mainloop()

# import customtkinter as ctk

# root = ctk.CTk()

# root.title("Hospital Management")
# root.geometry("500x400")

# label = ctk.CTkLabel(root, text="Patient Name")
# label.pack(pady=10)

# entry = ctk.CTkEntry(root, placeholder_text="Enter Name")
# entry.pack(pady=10)


# def add():
#     name = entry.get()
#     print(name)


# button = ctk.CTkButton(root, text="Add Patient", command=add)
# button.pack(pady=10)

# root.mainloop()

# import pyttsx3

# engine = pyttsx3.init()

# engine.say("Hello, welcome to Python")

# engine.runAndWait()


# import pyttsx3

# engine = pyttsx3.init()

# engine.setProperty("rate", 150)

# engine.say("Hello, I am learning Python")

# engine.runAndWait()

# import pyttsx3

# engine = pyttsx3.init()

# engine.setProperty("volume", 1.0)

# engine.say("Hello Python")

# engine.runAndWait()

# import pyttsx3

# engine = pyttsx3.init()

# engine.setProperty("rate", 150)
# engine.setProperty("volume", 1.0)

# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)

# engine.say("Hello, welcome to Hospital Management System")

# engine.runAndWait()

# from pynput import mouse

# def move(x, y):
#     print(x, y)

# listener = mouse.Listener(on_move=move)

# listener.start()
# listener.join()