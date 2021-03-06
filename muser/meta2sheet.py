from game_config import GLOB_CONFIG
from sheet.gen.meta_input import MetaInput
import os
import logger


def generate(sheet_path: str = os.path.abspath(GLOB_CONFIG.assets.getSheets())):

    if os.path.islink(sheet_path):
        sheet_path = os.readlink(sheet_path)

    logger.print(f"Generating sheets under {sheet_path}")

    file_list = os.listdir(sheet_path)
    for file in file_list:
        if file.endswith(".sheetmeta"):
            MetaInput.from_file(os.path.join(sheet_path, file)).proc()


if __name__ == "__main__":
    generate()
