#Je commence par importer le module tkinter ainsi que l'ensemble de ses éléments
from tkinter import *

#-----Création de l'interface graphique-----

window = Tk() #Création d'un objet qui représentera une interface
window.title("Morpion")#J'ajoute un titre à ma fenêtre
window.geometry("640x480")#Je veux une fenêtre d'une largeur de 640px et d'une haute de 480px
window.maxsize(800, 600)#Une taille max de 800px en largeur et 600px de hauteur
window.minsize(450, 300)#Une taille min de 450px de largeur et 300px de hauteur

#J'ajoute un message de bienvenue pour l'utilisateur
welcome_message = Label(window, text = "Bienvenue sur le jeu du morpion")
welcome_message.pack()

#Je demande à l'utilisateur si il souhaite choisir le cercle ou la croix pour débuter
make_you_choice = Label(window, text="Vous voulez commencer par le cercle ou la croix ?")
make_you_choice.place(y=40, x=220)


#Ajout de deux boutons, un qui représente le cercle, et l'autre la croix, pour donner le choix au joueur
first_choice = Button(window, text="O", command=lambda: get_choice("O"))
second_choice = Button(window, text="X", command=lambda: get_choice("X"))
first_choice.place(y= 80, x = 300)
second_choice.place(y = 80, x= 360)

#Ajout d'un message pour annoncer la victoire d'un joueur
you_win = Label(window, text= "")
you_win.place(y = 80, x = 440)


# La frame qui va contenir mon canvas
cadre = Frame(window, bg="white", width=500, height=500)
cadre.place(y = 120, x= 190)

#Je vais créer un tableau qui prendra la forme d'un Canvas
tableau = Canvas(cadre, bg="black", width=300, height=300)
tableau.grid(row=0, column=0, sticky="nsew")

#Je m'occupe de dessiner une grille au sein de mon canvas

#Je trace d'abord 2 lignes verticales
tableau.create_line(100, 0, 100, 300, width=3, fill="white")
tableau.create_line(200, 0, 200, 300, width=3, fill="white")

#Ensuite je trace 2 lignes horizontales
tableau.create_line(0, 100, 300, 100, width=3, fill="white")
tableau.create_line(0, 200, 300, 200, width=3, fill="white")

# ---- Déclaration des variables -----

#Je souhaite vérifier si une case est vide ou bien déjà occupée avant de pouvoir dessiner dessus
board = [0]*9
#Je créer une variable player, que j'initialise à "O"
player = "O"

#-------- Déclaration des fonctions ---------

#Je souhaite tout d'abord que l'utilisateur puisse soit commencer par le cercle, soit par la croix...
#Je déclare une première fonction pour récupérer le choix de l'utilisateur
def get_choice(your_choice): 
    global player #J'attribue une portée global à ma variable

    if your_choice == "O": #Si l'utilisateur choisi le cercle alors...
        player = "O"
    elif your_choice == "X": #Sinon il choisi la croix, alors...
        player = "X"
     
    #En choisisant l'un ou l'autre, les deux boutons vont être desactivés
    first_choice["state"] = "disabled"
    second_choice["state"] = "disabled"

#Ensuite je souhaite utiliser les click de la souris pour pouvoir tracer des cercles ou des croix...
def mouse_click(click):
    global player, board 
    x = click.x 
    y = click.y
    line = (y-2)//100
    column = (x-2)//100

    if board[line*3+column] == 0 :              #On vérifie si les 3 cases dans le tableau est vide
        if player == "O":                       #Si c'est au tour du cercle, alors...
            tableau.create_oval(100*column+8, 100*line+8, 100*column+96, 100*line+96, width=2, outline='#e13131')
            board[line*3+column] = 1            #Si c'est le cas, on dessine le cercle dans la liste
            player = "X"                        #l'autre joueur dessinera une croix
        else:                                   #Si c'est au tour de la croix, alors...
            tableau.create_line(100*column+8, 100*line+8, 100*column+96, 100*line+96, width=2, fill='#3145f0')
            tableau.create_line(100*column+8, 100*line+96, 100*column+96, 100*line+8, width=2, fill='#3145f0')
            board[line*3+column] = 2          #Sinon on dessiner une croix
            player = "O"
        
    check_victory() #J'apelle ma fonction check_victory, pour vérifier l'état du jeu après chaque tour

#Je déclare une fonction pour vérifier si un joueur remporte la victoire
def check_victory():
    global player, board
    #Je créer une liste de tuples qui contient toutes les combinaisons pour gagner
    win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    #Pour chaque symboles qui se retouve dans une des combinaisons de victoire...
    for symboles in win:

        if all(board[i] == 1 for i in symboles):
            you_win.config(text="Le premier joueur a gagné !")
        elif all(board[i] == 2 for i in symboles):
            you_win.config(text="Le second joueur a gagné !")
        elif all(case != 0 for case in board):
            you_win.config(text="C'est un match nul !")

# ---- Finalisation de l'interface ------

#J'ajoute une fonction pour recommencer la partie.

def retry():
    global player, board
    tableau.delete("all")
    board = [0]*9 #Je réinitialise le contenu de mon tableau
    player = "O" #Je réinitialise le joueur à cercle

    #Je réinitialise l'état des boutons 'X' et 'O' à active
    first_choice["state"] = "active" 
    second_choice["state"] = "active"

    you_win.config(text="") #J'efface aussi le message de victoire


    #Je retrace ensuite mes 2 lignes horizontale et vertical
    tableau.create_line(100, 0, 100, 300, width=3, fill="white")
    tableau.create_line(200, 0, 200, 300, width=3, fill="white")
    tableau.create_line(0, 100, 300, 100, width=3, fill="white")
    tableau.create_line(0, 200, 300, 200, width=3, fill="white")

#Et une fonction pour quitter la fenêtre
def quit():
    window.destroy


#La fonction retry va être appellé par le bouton recommencer
rejouer = Button(cadre, text="Recommencer", command=retry)
rejouer.grid(row=1, column=0, sticky="w", padx=55, pady=10)

#Tandis que la fonction quit va être appellé par le bouton exit
exit = Button(cadre, text="Quitter", command=quit)
exit.grid(row=1, column=0, sticky="e", padx=65, pady=10)

tableau.bind("<Button-1>", mouse_click) #Appel de la fonction mouse_click au click de la souris
window.mainloop() #Appel de l'ouverture de l'interface graphique