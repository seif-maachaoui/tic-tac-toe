#Je commence par importer le module tkinter ainsi que l'ensemble de ses éléments
from tkinter import *


#-----Création de l'interface graphique-----

window = Tk() #Création d'un objet qui représentera une interface
window.title("Morpion")#J'ajoute un titre à ma fenêtre
window.geometry("640x480")#Je veux une fenêtre d'une largeur de 640px et d'une haute de 480px
window.maxsize(800, 600)#Une taille max de 800px en largeur et 600px de hauteur
window.minsize(450, 300)#Une taille min de 450px de largeur et 300px de hauteur

#J'ajoute un message de bienvenue pour l'utilisateur
first_message = Label(window, text = "Bienvenue sur le jeu du morpion")
first_message.place()

make_you_choice = Label(window, text="Veuillez choisir, le cercle ou la croix ?")
make_you_choice.place(y=40, x=220)


#Ajout de deux boutons, un qui représente le cercle, et l'autre la croix, pour donner le choix au joueur
first_choice = Button(window, text="O")
second_choice = Button(window, text="X")
first_choice.place(y= 80, x = 300)
second_choice.place(y = 80, x= 330)

#--------Création d'une frame-------
cadre = Frame(window, bg="grey", width=500, height=500)
cadre.place(y = 120, x= 190)

#Je vais créer un canvas qui va contenir mon tableau pour le morpion
tableau = Canvas(cadre, bg="black", width=301, height=301)
tableau.grid(row=0, column=0, sticky="nsew")

#--------Mise en place de la grille------

#Je trace d'abord 2 lignes verticales
tableau.create_line(100, 0, 100, 300, width=3, fill="white")
tableau.create_line(200, 0, 200, 300, width=3, fill="white")

#Ensuite je trace 2 lignes horizontales
tableau.create_line(0, 100, 300, 100, width=3, fill="white")
tableau.create_line(0, 200, 300, 200, width=3, fill="white")

#--------Déclaration des fonctions---------

def mouse_position(event):
    x = event.x
    y = event.y
    print("Position de la souris: x = {}, y = {}".format(x, y), end="\r")

def mouse_click(click):
    x = click.x
    y = click.y
    print("Clic de souris: x = {}, y = {}".format(x, y), end="\r")



tableau.bind("<Motion>", mouse_position) #Appel de la fonction mouse_position au déplaçement de la souris
tableau.bind("<Button-1>", mouse_click) #Appel de la fonction mouse_click au click de la souris
window.mainloop()