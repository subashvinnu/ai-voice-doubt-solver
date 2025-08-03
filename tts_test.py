from elevenlabs import ElevenLabs, play

api_key = "sk_d8d152a907bffbd400af0bab528ca9bb6f7a5e9b73a81f0a"  # replace with your key

client = ElevenLabs(api_key=api_key)

# List available voices to get correct name
voices = client.voices()
print("Available voices:")
for voice in voices:
    print(f"{voice.name} - {voice.voice_id}")

# Pick a real voice name like "Bella"
voice_name = "Bella"

# Generate speech
audio = client.generate(text="Hello Subash! AI Voice Explainer is ready.", voice=voice_name)

# Play the audio
play(audio)


