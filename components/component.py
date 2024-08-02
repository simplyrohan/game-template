import pygame
import scenes.scene


class Component:
    def __init__(self) -> None:
        self.current_scene = None

        self.rect = None

    def update(self, screen: pygame.Surface, events: list[pygame.Event], dt: int):
        pass

    def close(self):
        self.current_scene.components.remove(self)