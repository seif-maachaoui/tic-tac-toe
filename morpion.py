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
second_choice.place(y = 80, x= 330)

#Ajout d'un message pour annoncer la victoire d'un joueur
you_win = Label(window, text= "")
you_win.place(y = 80, x = 420)


# La frame qui va contenir mon canvas
cadre = Frame(window, bg="grey", width=500, height=500)
cadre.place(y = 120, x= 190)

#Je vais créer un tableau qui prendra la forme d'un Canvas
tableau = Canvas(cadre, bg="black", width=300, height=300)
tableau.grid(row=1, column=0, sticky="nsew")

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
            player = "O"                        #L'autre joueur dessinera un cercle

#Je déclare une fonction pour vérifier si le joueur remporte la victoire
def check_victory():
    global board 

    #Vérification des lignes horizontal
    for i in range (0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != 0: #Si une ligne horizontal est remplie, alors..
            return True
    
    #Vérification des lignes vertical
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != 0 : #Si une ligne vertical est remplie, alors...
            return True

    #Vérification des diagonale de gauche à droite
    if board[0] == board[4] == board[8] != 0:
        return True
    #Vérification de la diagonale de droite à gauche
    if board[2] == board[4] == board[6] and board[2] != 0:
        return board[2]
    
    #Vérification de match nul 
    if 0 not in board: #Si toutes les cases sont occupées et qu'aucun joueur n'a gagné, alors...
        return 0 #match nul
    return None
tableau.bind("<Button-1>", mouse_click) #Appel de la fonction mouse_click au click de la souris
window.mainloop()