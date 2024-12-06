import pygame as pg

class Sounds:
    def __init__(self):
        """
        Initialize and load sound effects for the game.
        """
        # Initialize the Pygame mixer
        pg.mixer.init()

        # Load sounds
        self.collect_sound = pg.mixer.Sound("grain_collect.wav")
        self.explode_sound = pg.mixer.Sound("bucket_explode.wav")

        # Set default volumes (optional)
        self.collect_sound.set_volume(0.5)  # Volume: 0.0 to 1.0
        self.explode_sound.set_volume(0.8)

    def play_grain_collect(self):
        """
        Play the grain collection sound.
        """
        self.collect_sound.play()

    def play_bucket_explode(self):
        """
        Play the bucket explosion sound.
        """
        self.explode_sound.play()
        
