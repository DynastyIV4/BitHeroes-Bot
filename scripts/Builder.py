import subprocess
import os
import sys

# Paths
script_name = "BitHeroes-Bot.py"
data_folder = os.path.abspath("data")
script_folder = os.path.abspath("scripts")
icon_path = rf"{data_folder}\images\window_icon.ico"
output_dir = rf"{script_folder}\output"
build_dir = rf"{output_dir}\build"
spec_dir = rf"{output_dir}\spec"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Construct PyInstaller command
command = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--noconsole",
    f"--icon={icon_path}",
    f"--add-data={data_folder}{';' if os.name == 'nt' else ':'}data",
    f"--distpath={output_dir}",
    f"--workpath={build_dir}",
    f"--specpath={spec_dir}",
    script_name,
]


# Run the command and stream output
print("Running PyInstaller build...")
result = subprocess.run(command, stdout=sys.stdout, stderr=sys.stderr)
if (result):
    print("Build complete! ✅")
else:
    print("Build failed.. ❌")
