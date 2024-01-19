YouTube Shorts Generator

This project automates the creation of YouTube Shorts with custom audio and subtitles, combining video editing capabilities of MoviePy, precise audio transcription from Whisper with timestamp features, and the TikTok voice API for speech generation.
Features

    Automated Video and Music Selection: Selects video clips and music tracks from the resources directory.
    Custom Audio Generation: Uses the TikTok voice API for creating speech.
    Enhanced Audio Transcription: Employs Whisper with timestamp support for detailed transcription.
    Dynamic Subtitle Generation: Dynamically adds subtitles based on the detailed transcription.
    Credit Attribution: Automatically attributes credits for selected video and music.

Project Structure

graphql

YOUTUBE SHORTS PROJECT
│
├── resources/                     # Directory for video, audio resources and script
├── tiktok-voice-main/             # TikTok voice API integration
├── whisper-timestamped-master/    # Whisper module for timestamped transcriptions
├── audio.py                       # Script for audio generation
├── Demo-Short.mp4                 # Example video file
├── main.py                        # Main script for generating YouTube Shorts
├── readme.md                      # Project documentation (this file)
├── requirements.txt               # Required Python libraries
└── transcribe.py                  # Script for detailed transcription

Requirements

    Python 3.x
    MoviePy
    Whisper (with timestamp support)
    TikTok Voice API
    ImageMagick (for MoviePy compatibility)

Setup

    Install Dependencies:
        Install Python 3.x.
        Install necessary libraries from requirements.txt using pip install -r requirements.txt.
        Set up ImageMagick according to main.py.

    Configuration:
        Add video and audio files to the resources directory.
        Adjust file paths and settings in main.py as needed.

Usage

    Run main.py to generate a YouTube Short. The script will handle audio generation, transcription, subtitle creation, and video editing.

Dependencies and Credits

    TikTok Voice API: For audio generation capabilities. TikTok Voice API Repository.
    Whisper Timestamped: For detailed audio transcription with timestamps. This project is an enhancement of the original Whisper model by OpenAI, providing additional functionality for timestamped transcription. Whisper Timestamped Repository.
    Idea Inspiration: Yellojello's YouTube Channel.
    TikTok Voice API Creation: By Oscie.