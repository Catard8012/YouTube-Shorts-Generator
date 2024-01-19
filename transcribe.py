import whisper_timestamped
import json

def transcribe_and_extract_timestamps(audio_file):
    # Load the Whisper model
    model = whisper_timestamped.load_model("base", device="cpu")

    # Load the audio file
    audio = whisper_timestamped.load_audio(audio_file)

    # Transcribe the audio file
    result = whisper_timestamped.transcribe(model, audio)

    # Extract word-level timestamps
    timestamps = []
    for segment in result.get('segments', []):
        for word_info in segment.get('words', []):
            timestamps.append({
                "word": word_info['text'],
                "start": word_info['start'],
                "end": word_info['end'],
                "confidence": word_info['confidence']
            })

    # Save the timestamps to a JSON file
    with open("word_timestamps.json", "w") as file:
        json.dump(timestamps, file, indent=4)

    print("\033[92mTranscript Complete\033[0m \n")

# Path to your WAV file
audio_file = 'output.mp3'

# Transcribe and extract timestamps
transcribe_and_extract_timestamps(audio_file)
