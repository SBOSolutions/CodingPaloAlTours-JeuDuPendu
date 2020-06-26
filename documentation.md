## Deroulement de l'atelier

#### Mise en place de la fenetre pygame

```python
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

```

#### Mise en place de la boucle d'affichage de la fenetre 

```python
# Boucle de jeu
run = True # variable boolean precisant que le jeu tourne
while run:
    for event in pygame.event.get(): # boucle for pour capturer les evenements de la fenetre
        if event.type == pygame.QUIT:
            run = False
```

#### Mise en place d'une fonction d'affichage
```python
# mise en place d'une fonction d'affichage

def draw():
    window.fill((255,255,255))
    pygame.display.update()

```

ajout de l'appel de la fonction dans la boucle de jeu.
definition d'une section de couleur pour definir les couleur sous forme de variable.




### PARKING

```python

```