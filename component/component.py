import pygame
import scenes.scene


class Component:
    def __init__(self) -> None:
        self.current_scene = None

        self.position = pygame.Vector2(0, 0)

    def update(self, events: list[pygame.Event], dt: int):
        pass

    def close(self):
        self.current_scene.components.remove(self)
