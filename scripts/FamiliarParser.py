from bs4 import BeautifulSoup
from collections import defaultdict
import json
import os
import re

file_path = os.path.join(os.path.dirname(__file__), "familiar_parser_files/wiki.html")

with open(file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

RARITY_KEY = "rarity"
QUEST_KEY = "quest"
ZONE_KEY = "zone"
DUNGEON_KEY = "dungeon"
RAID_KEY = "raid"

familiars_dict = defaultdict(lambda: {QUEST_KEY: {ZONE_KEY: [], DUNGEON_KEY: []}, RAID_KEY: {ZONE_KEY: []}, RARITY_KEY: ""})
QUEST_KEYT = "quest"
ZONE_KEY = "zone"
DUNGEON_KEY = "dungeon"
RAID_KEY = "raid"

tables = soup.find_all("table", {"class": "mw-collapsible bittable grey3 mw-made-collapsible"})  

for table in tables:
    rows = table.find_all("tr")
    rarity = table.find("caption").text.strip().split()[0].lower()

    for row in rows:
        td_list = row.find_all("td")
        if row.has_attr("id"):
            familiar_name = td_list[1].text.strip()
            if familiar_name:
                familiars_dict[familiar_name][RARITY_KEY] = rarity
                pass
                
        for td in td_list:
            text = td.text.strip()
            match_quest = re.match(r"Z(\d+)D(\d+)", text)
            if match_quest:
                zone_dungeons = text.split("/")
                for zone_dungeon in zone_dungeons:
                    match_quest = re.match(r"Z(\d+)D(\d+)", zone_dungeon)
                    zone, dungeon = match_quest.groups()
                    familiars_dict[familiar_name][QUEST_KEY][ZONE_KEY].append(zone)
                    familiars_dict[familiar_name][QUEST_KEY][DUNGEON_KEY].append(dungeon)
                break
            match_raid = re.match(r"R(\d+)", text)
            if match_raid:
                raids = text.split("/")
                for raid in raids:
                    match_raid = re.match(r"R(\d+)", raid)
                    raid = match_raid.group(1)
                    familiars_dict[familiar_name][RAID_KEY][ZONE_KEY].append(raid)
                break
                

output_file_path = os.path.join(os.path.dirname(__file__), "familiar_parser_files/output/familiar_data.json")
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(familiars_dict, output_file, indent=4)
print(f"Output written to {output_file_path}")