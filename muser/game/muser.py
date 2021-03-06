import pyxel
from game.config import Config
import traceback
import logger
from pyglet import clock


class Muser:
    def __init__(self):
        from game.casts import Casts
        Config.CAST = Casts.Intro()
        pyxel.run(self.update, self.draw)

    def update(self):
        try:
            if Config.CAST.is_finished():
                Config.CAST = Config.CAST.next_cast()
                logger.debug(
                    "Scene " + type(Config.CAST).__name__ + " in.")
            clock.tick()
            Config.CAST.update()
        except BaseException as e:
            logger.print(e)
            traceback.print_exc()
            exit()

    def draw(self):
        Config.CAST.clear_screen()
        Config.CAST.draw()
