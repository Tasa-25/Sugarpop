import pygame as pg

class Sounds:
    def __init__(self):
        """
        Initialize and load sound effects for the game.
        """
        # Initialize the Pygame mixer
        pg.mixer.init()

        # Load sounds
        self.collect_sound = pg.mixer.Sound("./sounds/sugarpop1.mp3")
        self.explode_sound = pg.mixer.Sound("./sounds/sugarpop2.mp3")

        # Set default volumes (optional)
        self.collect_sound.set_volume(0.5)  # Volume: 0.0 to 1.0
        self.collect_channel = pg.mixer.Channel(0)
        self.explode_sound.set_volume(0.8)
        self.explode_channel = pg.mixer.Channel(1)

    def play_grain_collect(self):
        """
        Play the grain collection sound.
        """
        self.collect_channel.play(self.collect_sound)
        
    def play_bucket_explode(self):
        """
        Play the bucket explosion sound.
        """
        self.explode_channel.play(self.explode_sound)
        
