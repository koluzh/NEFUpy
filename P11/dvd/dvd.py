from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.core.text import Label as CoreLabel


class DVD(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.label.pos = self.pos


class DVDBounce(Widget):
    dvd = ObjectProperty(None)

    def serve_dvd(self):
        self.dvd.center = self.center
        self.dvd.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.dvd.move()
        if self.dvd.x < 0 or self.dvd.right > self.width:
            self.dvd.velocity_x *= -1
        if self.dvd.y < 0 or self.dvd.top > self.height:
            self.dvd.velocity_y *= -1


class DVDApp(App):
    def build(self):
        game = DVDBounce()
        game.serve_dvd()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    DVDApp().run()