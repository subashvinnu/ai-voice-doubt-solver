from elevenlabs.client import ElevenLabs

# ✅ Create the ElevenLabs client with your API key
client = ElevenLabs(
    api_key="sk_d8d152a907bffbd400af0bab528ca9bb6f7a5e9b73a81f0a"  # Replace with your key if needed
)

# ✅ Get the list of voices
voice_list = client.voices.get_all().voices  # `.voices` gives you a proper list

print("Available Voices:")

# ✅ Print each voice name and ID
for voice in voice_list:
    print(f"{voice.name} - {voice.voice_id}")










