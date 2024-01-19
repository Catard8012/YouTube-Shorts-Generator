import subprocess

# Define the command you want to execute
command = [
    "py", "tiktok-voice-main\main.py", 
    "-v", "en_us_006",
    "-f", "resources\script.txt", # Add the Scrit Here
    "-n", "output.mp3", 
    "--session", "73782eef66d5ab64bf83342be9623375"
]

# Execute the command
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output
print("Output:", process.stdout.decode())
print("\033[92mAudio Complete\033[0m \n")
