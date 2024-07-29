import pygame
import component.component

class Scene:
    def __init__(self):
        self.components: list[component.Component] = []

    def update(self, events: list[pygame.Event], dt: int):
        for component in self.components:
            component.current_scene = self
            component.update(events, dt)

        return self

    def close(self):
        for component in self.components:
            component.close()
