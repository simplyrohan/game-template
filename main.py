import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Untitled Game")

clock = pygame.time.Clock()

dt = 0

scene = None  # Change this to the first scene

running = True
while running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Background Color

    # Update the scene
    if scene is not None:
        scene = scene.update(events, dt)
    else:
        running = False

    pygame.display.flip()
    dt = clock.tick(60)  # Change this to FPS

pygame.quit()
