import pygame
import math

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

# Police de caratère
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
MOT_FONT = pygame.font.SysFont('comicsans', 60)
TITRE_FONT = pygame.font.SysFont('comicsans', 100)

# chargement des images potence
images = [] # on créer un liste des images
# alimentation de la list avec les images de pendu
for i in range(7):
    image = pygame.image.load("images/pendu" + str(i) + ".png")
    images.append(image)

# ajout des lettres de l'alphabet
RAYON = 20
ECART = 15
lettres = [] # liste pour les lettres
startX = round( (WIDTH - (RAYON * 2 + ECART) * 13) / 2 )  # formule math pour position X sur la fenetre
startY = 500
A = 65 # la lettre A dans les chr est à la position 64 et ainsi de suite

for i in range(26): # pour les 26 lettre de l'alphabet
    x = startX + ECART * 2 + ((RAYON * 2 + ECART) * (i%13)) # pour la gestion de la ligne 2
    y = startY + ((i//13) * (ECART + RAYON * 2))
    lettres.append([x, y, chr(A + i), True])  # liste avec coordonnées x, y, la valeur ascii de la lettre, et si visible True/False

# variables du jeu
penduStatut = 0
mot = "CODING"
lettreDevinee = []

# mise en place d'une fonction d'affichage
def draw():
    window.fill(WHITE) # couleur du fond
    window.blit(images[penduStatut], (150,100))

    # dessin du mot
    afficheMot = ""
    for lettre in mot:
        if lettre in lettreDevinee:
            afficheMot += lettre + " "
        else:
            afficheMot += "_ "
    text = MOT_FONT.render(afficheMot, 1, BLACK)
    window.blit(text, (400, 200))

    # dession des lettres
    for lettre in lettres:
        x, y, ltr, visible = lettre #decompose
        if visible:
            pygame.draw.circle(window, BLACK, (x,y), RAYON, 3) # pour les ronds - fenetre, couleur, coordonnées, rayon, epaisseur du trait
            # utilisation de la fonction render
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    pygame.display.update()

def afficheMessage(message):
    pygame.time.delay(1000)
    window.fill(BLACK)
    text = TITRE_FONT.render(message, 1, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

# Boucle de jeu
run = True # variable boolean precisant que le jeu tourne
while run:
    for event in pygame.event.get(): # boucle for pour capturer les evenements de la fenetre
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for lettre in lettres:
                x, y, ltr, visible = lettre # decompose
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2) # pythagore
                    if dis < RAYON:
                        lettre[3] = False
                        lettreDevinee.append(ltr)
                        if ltr not in mot:
                            penduStatut += 1
    draw()    
    gagne = True
    for lettre in mot:
        if lettre not in lettreDevinee:
            gagne = False
            break

    if gagne:
        afficheMessage("Gagné !")
        break

    if penduStatut == 6:
        afficheMessage("Perdu !")
        break