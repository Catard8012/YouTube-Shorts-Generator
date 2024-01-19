# YouTube Shorts Generator

Welcome to my YouTube Shorts Generator! This is a fun little tool I made for creating YouTube Shorts with custom audio and subtitles. It's one of my first projects, and I'm excited to share it with the community.

# Project Contents

    main.py: The heart of the generator, orchestrating the creation process.
    audio.py: Script for generating audio using the TikTok voice API.
    transcribe.py: Transcribes the generated audio with timestamps.
    Demo-Short.mp4: A demo video to show you what this script can do.
    readme.md: This file, explaining how everything works.
    requirements.txt: Lists all the Python libraries you'll need.

# Setting Up

    Create a 'resources' folder: This is where you'll need to place your video clips, music files, and a script.txt file for the audio narration.

    Install Dependencies:
        Make sure you have Python 3.x installed.
        Install the necessary Python libraries with pip install -r requirements.txt.
        You'll need to set up tiktok-voice-main and whisper-timestamped-main separately. Check their respective repositories for installation instructions.

    Prepare Your Files:
        Add your choice of video and audio files to the resources folder.
        Write the script for your audio in script.txt within the resources folder.

# How to Use

Run main.py to start creating your YouTube Short. The script will use your video and audio files from the resources folder, generate audio using the text from script.txt, transcribe this audio, and compile everything into a cool short video.

# Credits

    This project is inspired by Yellojello YouTube videos.
    Big thanks to the teams behind the TikTok voice API and Whisper for their fantastic tools.
