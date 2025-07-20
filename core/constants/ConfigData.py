from core.ExecutableUtilities import ExecutableUtilities
import os

# =======================
# PATHS 
# =======================

DATA_PATH = ExecutableUtilities.resource_path("data")
BOT_HEROES_APPDATA_PATH = rf"{os.getenv('APPDATA')}\BotHeroes"
FONT_PATH = rf"{DATA_PATH}\fonts"
AUTO_QUEST_DATA_FILE = rf"{BOT_HEROES_APPDATA_PATH}\auto_quest_settings.json"
AUTO_FISH_DATA_FILE = rf"{BOT_HEROES_APPDATA_PATH}\auto_fish_settings.json"
GENERAL_SETTINGS_DATA_FILE = rf"{BOT_HEROES_APPDATA_PATH}\general_settings.json"
FAMILIAR_DATA_PATH = rf"{DATA_PATH}\familiars.json"
EDIT_UNDO_FONT_PATH = rf"{FONT_PATH}\editundo.ttf"
PIXEL_DIGIVOLVE_FONT_PATH = rf"{FONT_PATH}\Pixel Digivolve.otf"
TESSERACT_PATH = rf"{DATA_PATH}\tesseract\tesseract.exe"
APPDATA_FOLDER = "BotHeroes"

# =======================
# GAME SETTINGS 
# =======================

BIT_HEROES_PROCESS_NAME = "Bit Heroes.exe"
BIT_HEROES_WINDOW_TITLE = "Bit Heroes"
BOT_HEROES_WINDOW_TITLE = "Bot Heroes"

# =======================
# URLs 
# =======================

GITHUB_URL = "https://github.com/elwoujdi/BotHeroes/issues/new/choose"
DISCORD_URL = "https://discord.gg/KewWWyEm"
WIKI_URL = "https://github.com/elwoujdi/BotHeroes?tab=readme-ov-file#readme"
