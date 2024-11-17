import pygame
import random

def draw_grid(chosen_screen):

    #initial coordinates set to 32 b/c there's no use in drawing a line on the edge of the screen
    y_coor = 32
    x_coor = 32

    # draw horizontal lines
    for i in range(1, 16):
        pygame.draw.line(chosen_screen,
                         "black",
                         (0,i*y_coor),
                         (640,i*y_coor),
                         1)

    #draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(chosen_screen,
                         "black",
                         (i*x_coor, 0),
                         (i*x_coor, 512),
                         1)

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((640, 512))

        screen.fill("light green") #making the screen light green
        draw_grid(screen) #drawing the lines


        #drawing mole:
        mole_image = pygame.image.load("mole.png")

        mole_x = 0
        mole_y = 0
        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

        clock = pygame.time.Clock()
        pygame.display.flip()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (mole_x <= event.pos[0] <= mole_x + 32) and (mole_y <= event.pos[1] <= mole_y +32):
                        #reset screen with new mole:
                        screen.fill("light green")
                        draw_grid(screen)

                        mole_x = random.randrange(0, 20)*32
                        mole_y = random.randrange(0, 16)*32
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
                        pygame.display.flip()

            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
