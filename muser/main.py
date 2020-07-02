import pyxel
import os
import game_config as game_config
import logger

pyxel.init(256, 256,
           caption="Muser",
           fps=game_config.GLOB_CONFIG.config["fps"],
           fullscreen=game_config.GLOB_CONFIG.config["full_screen"])

logger.print("Window loaded")
res_path = os.path.join(
    game_config.GLOB_CONFIG.assets.root, "resources.pyxres")
pyxel.load(res_path)
logger.print(f"Res loaded: {os.path.abspath(res_path)}")
from game import muser  # noqa: E402, F401
