import pygame



class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((9, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -5
        self.speedy = -5
        self.direcao = direcao
    def update(self):
        if self.direcao == 'esquerda':
            self.rect.x += self.speedx
        else:
            self.rect.x -= self.speedx
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()