from core.ExecutableUtilities import ExecutableUtilities
import os

# =======================
# VERSION 
# =======================

VERSION = "v.1.0.1"

# =======================
# PATHS 
# =======================

APPDATA_FOLDER = "BitHeroes-Bot"
DATA_PATH = ExecutableUtilities.resource_path("data")
BIT_HEROES_BOT_APPDATA_PATH = rf"{os.getenv('APPDATA')}\{APPDATA_FOLDER}"
FONT_PATH = rf"{DATA_PATH}\fonts"
AUTO_QUEST_DATA_FILE = rf"{BIT_HEROES_BOT_APPDATA_PATH}\auto_quest_settings.json"
AUTO_FISH_DATA_FILE = rf"{BIT_HEROES_BOT_APPDATA_PATH}\auto_fish_settings.json"
GENERAL_SETTINGS_DATA_FILE = rf"{BIT_HEROES_BOT_APPDATA_PATH}\general_settings.json"
FAMILIAR_DATA_PATH = rf"{DATA_PATH}\familiars.json"
EDIT_UNDO_FONT_PATH = rf"{FONT_PATH}\editundo.ttf"
PIXEL_DIGIVOLVE_FONT_PATH = rf"{FONT_PATH}\Pixel Digivolve.otf"
TESSERACT_PATH = rf"{DATA_PATH}\tesseract\tesseract.exe"

# =======================
# GAME SETTINGS 
# =======================

BIT_HEROES_PROCESS_NAME = "Bit Heroes.exe"
BIT_HEROES_WINDOW_TITLE = "Bit Heroes"
BIT_HEROES_BOT_WINDOW_TITLE = "Bit Heroes Bot"

# =======================
# URLs 
# =======================

GITHUB_URL = "https://github.com/elwoujdi/BitHeroes-Bot/issues/new/choose"
DISCORD_URL = "https://discord.gg/yBBrUAd5zj"
WIKI_URL = "https://github.com/elwoujdi/BitHeroes-Bot?tab=readme-ov-file#readme"
