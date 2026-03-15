from extract_audio import extract_audio
from transcribe import transcribe_audio
from summarize import generate_notes

video_path = "uploads/test1.mp4"
audio_path = "outputs/audio.wav"

print("Extracting audio...")
extract_audio(video_path, audio_path)

print("Transcribing audio...")
transcript = transcribe_audio(audio_path)

print("Generating notes...")
notes = generate_notes(transcript)

print("\nFINAL NOTES:\n")
print(notes)

with open("outputs/notes.txt", "w", encoding="utf-8") as f:
    f.write(notes)