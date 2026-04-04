import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Adding image and background image')

bg= pygame.transform.scale(

pygame.image.load('Ln31\python4-game.png').convert(),

(WIDTH, HEIGHT))

img = pygame.transform.scale(

pygame.image.load('Ln31\player_01.png').convert_alpha(), (200, 200))

img_rect = img.get_rect(center=(WIDTH // 2,

HEIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render('Hello World ', True,

pygame.Color('black'))

text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 110))

def game_loop():

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

             running = False

        screen.blit(bg, (0, 0))

        screen.blit(img,img_rect)

        screen.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':

    game_loop()

