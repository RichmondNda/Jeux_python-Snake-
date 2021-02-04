import sys
import random
import pygame
import os


class jeu:
    
    # COntenir toutes les variables ainsi que les fonctions utilies pour le jeux 

    def __init__(self):
        self.ecran = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("JEU SNAKE N2R ")

        self.jeu_enCours = True

        # Les varaibles de position
        self.serpent_position_x = 300
        self.serpent_position_y = 300

        # VAraibles de direction

        self.serpent_direction_x = 0
        self.serpent_direction_y = 0

        self.serpent_corps = 10

        # Creation de la pomme

        self.pomme_position_x = random.randrange(110, 690, 10)
        self.pomme_position_y = random.randrange(110, 590, 10)
        self.pomme = 10

        # Gestion du fps

        self.clock = pygame.time.Clock()

        # Creation de la liste permettant de garder la tete du serpent

        self.positions_serpent = []

        #

        self.taille_du_serpent = 1

        # Ecran du debut

        self.ecran_du_debut = True
        self.ecran_de_fin = True

        # Image

        self.image = pygame.image.load(os.path.join('/home/regis/MesProjets/CoursPython/Jeux_Snake', 'start_snake.png'))
        self.image_transform = pygame.transform.scale(self.image, (790, 580))

        self.image_end = pygame.image.load(os.path.join('/home/regis/MesProjets/CoursPython/Jeux_Snake', 'end_snake.png'))
        self.image_end_transform = pygame.transform.scale(self.image_end, (790, 580))

        self.score = 0

        self.level = 15

    def fonction_principale(self):

        # ecran du debut

        while self.ecran_du_debut:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        # print("bjr")
                        self.ecran_du_debut = False

                self.ecran.fill((0, 0, 0))

                self.ecran.blit(self.image_transform, (5, 5, 5, 5))

                pygame.display.flip()

        # permet de gerer les evenement et les composants du jeux grace a la boucle while loop

        while self.jeu_enCours:

            for event in pygame.event.get():

                # Permet de savoir si kle jeux est encore en cours
                if event.type == pygame.QUIT:
                    sys.exit()

                # Les evenement qui permettent de faire bouger le serpent

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:

                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0
                        # print('right')

                    if event.key == pygame.K_LEFT:

                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                        # print('left')

                    if event.key == pygame.K_DOWN:

                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 10
                        # print('down')

                    if event.key == pygame.K_UP:

                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -10
                        # print('up')
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

            if ((self.serpent_position_x <= 100) or (self.serpent_position_x >= 700) or (self.serpent_position_y <= 100) or (self.serpent_position_y >= 600)):
                self.jeu_enCours = False

                # Faire bouger le serpent

            # cree la condition pour faire bouger la pomme

            if ((self.pomme_position_x == self.serpent_position_x) and (self.pomme_position_y == self.serpent_position_y)):
                self.pomme_position_x = random.randrange(110, 690, 10)
                self.pomme_position_y = random.randrange(110, 590, 10)

                self.score += 1

                # Augmantation de la taille du serpent

                self.taille_du_serpent += 1


            # Cree une liste qui stocke la position de la tete du serpent

            tete_du_serpent = []
            tete_du_serpent.append(self.serpent_position_x)
            tete_du_serpent.append(self.serpent_position_y)

            # aPpend dans la liste des positions

            self.positions_serpent.append(tete_du_serpent)

            if len(self.positions_serpent) > self.taille_du_serpent:
                self.positions_serpent.pop(0)

            # remplissage de la couleur de l'ecran
            self.ecran.fill((0, 0, 0))

            # Afficher le serpent

            pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))

            # Afficher les autres parties du serpent

            for partie_serpent in self.positions_serpent:
                pygame.draw.rect(self.ecran, (0, 255, 0), (partie_serpent[0], partie_serpent[1], self.serpent_corps, self.serpent_corps))

            # AU cas ou le serpent se mord

            for partie_serpent in self.positions_serpent[:-1]:
                if (partie_serpent == tete_du_serpent):
                    self.jeu_enCours = False

            # Afficher la pomme

            if self.score == 20:
                self.level += 5
            elif self.score == 40:
                self.level += 5
            elif self.score == 60:
                self.level += 5
            elif self.score == 80:
                self.level += 5

            pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

            self.cree_message('grande', 'Snake Game', (320, 10, 100, 50), (255, 255, 255))
            self.cree_message('moyenne', ' Score  : {}'.format(str(self.score)), (375, 50, 50, 50), (255, 255, 255))

            self.create_limites()
            self.clock.tick(self.level)
            pygame.display.flip()

        # ecran de fin

        while self.ecran_de_fin:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        # print("bjr")
                        self.ecran_de_fin = False

                self.ecran.fill((0, 0, 0))

                self.ecran.blit(self.image_end_transform, (5, 5, 5, 5))

                pygame.display.flip()

    def create_limites(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 100, 600, 500), 3)

    def cree_message(self, font, message, message_rectangle, couleur):

        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20, False)

        if font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, True)

        if font == 'grande':
            font = pygame.font.SysFont('Lato', 40, False)

        message = font.render(message, True, couleur)

        self.ecran.blit(message, message_rectangle)


if __name__ == '__main__':

    pygame.init()

    jeu().fonction_principale()

    pygame.quit()
