from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"path/to/ImageMagick-7.1.1-Q16-HDRI/magick.exe"}) # Add your path to magick.exe

import subprocess
import random
import moviepy.editor as mp
import os
import json

# Run audio and transcription scripts
subprocess.run(['python', 'audio.py'])
subprocess.run(['python', 'transcribe.py'])

# Load transcription data
with open('word_timestamps.json', 'r') as file:
    transcription = json.load(file)

# Paths to video files, audio file, and songs
video_files = ["resources/your_video1.mp4", "resources/your_video2.mp4", "resources/your_video3.mp4"] # Add your videos
audio_path = "output.mp3"
songs = ['resources/your_song1.mp3', 'resources/your_song2.mp3'] # Add your songs

# Randomly choose a video and a song
chosen_video = random.choice(video_files)
chosen_song = random.choice(songs)

video = mp.VideoFileClip(chosen_video)
audio = mp.AudioFileClip(audio_path)
song = mp.AudioFileClip(chosen_song)

# Print the chosen video and song
print(f"\033[92mSelected video: {chosen_video}\033[0m")
print(f"\033[92mSelected song: {chosen_song}\033[0m \n")

# Adjust song length to match the audio file's duration
song = song.subclip(0, audio.duration)

# Check audio duration and set a random start point in the video
audio_duration = audio.duration
max_start_time = video.duration - audio_duration
start_time = random.uniform(0, max_start_time)

# Crop the video to match the audio duration
video_cropped = video.subclip(start_time, start_time + audio_duration)

# Function to add a batch of subtitles
def add_subtitles_to_clip(video_clip, subtitles_batch):
    clips = [video_clip]
    for subtitle in subtitles_batch:
        start, end = subtitle['start'], subtitle['end']
        txt_clip = mp.TextClip(subtitle['word'], fontsize=110, color='white', font='Arial-Bold')
        txt_clip = txt_clip.set_position('center').set_duration(end - start).set_start(start)
        clips.append(txt_clip)
    return mp.CompositeVideoClip(clips)

# Process subtitles in batches
batch_size = 100  # Adjust based on performance
batches = [transcription[i:i + batch_size] for i in range(0, len(transcription), batch_size)]

final_clip = video_cropped
for batch in batches:
    final_clip = add_subtitles_to_clip(final_clip, batch)

# Set the audio of the video to be a combination of the selected song and the generated audio
final_clip_with_audio = final_clip.set_audio(mp.CompositeAudioClip([song, audio]))

# Export the final video
output_path = "output_video.mp4"
final_clip_with_audio.write_videofile(output_path, codec='libx264')

print(f"\033[92mVideo with subtitles created: {output_path}\033[0m \n")

# Delete temporary files
os.remove(audio_path)
print(f"\033[92m{audio_path} deleted.\033[0m")
os.remove('word_timestamps.json')
print(f"\033[92mword_timestamps.json deleted.\033[0m")
