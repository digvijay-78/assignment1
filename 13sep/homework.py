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

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

