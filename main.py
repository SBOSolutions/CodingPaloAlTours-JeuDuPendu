import pygame

# initiatlisation de pygame
pygame.init()

# mise en place et affichage de la fenetre de jeu

# constante pour la dimension de la fenetre
WIDTH = 800 # largeur
HEIGHT = 600 # hauteur

window = pygame.display.set_mode((WIDTH, HEIGHT))  # instruction pygame.display.set_mode((x,y)) pour la définition de la fenetre => dans une variable
pygame.display.set_caption("Nom de la fenetre") # ajout d'un nom à la fenetre
icon = pygame.image.load('gaming.png') #affectation d'une image dans une variable
pygame.display.set_icon(icon) # mise en place de l'image sur la fenetre


#Couleurs
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,150,0)
RED = (150,0,0)

# mise en place d'une fonction d'affichage

def draw():
    window.fill(WHITE)
    pygame.display.update()






# Boucle de jeu
run = True # variable boolean precisant que le jeu tourne
while run:
    draw()
    for event in pygame.event.get(): # boucle for pour capturer les evenements de la fenetre
        if event.type == pygame.QUIT:
            run = False