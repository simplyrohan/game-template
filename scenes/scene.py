import pygame
import components.component as component


class Scene:
    def __init__(self):
        self.components: list[component.Component] = []

    def update(self, screen: pygame.Surface, events: list[pygame.Event], dt: int, mouse_pos: pygame.Vector2):
        for component in self.components:
            component.current_scene = self
            component.update(screen, events, dt, mouse_pos)

        return self

    def close(self):
        for component in self.components:
            component.close()