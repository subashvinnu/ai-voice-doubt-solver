import streamlit as st
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os

load_dotenv()  # Load API key and voice ID from .env

# Load credentials
api_key = os.getenv("sk_d8d152a907bffbd400af0bab528ca9bb6f7a5e9b73a81f0a")
voice_id = os.getenv("VOICE_ID")

# Initialize ElevenLabs client
client = ElevenLabs(api_key=api_key)

st.title("🎧 AI Voice Explainer with ElevenLabs")
user_input = st.text_area("Enter the text to explain:")

if st.button("Generate Voice"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # Generate audio
            audio_stream = client.text_to_speech.convert(
                voice_id=voice_id,
                model_id="eleven_monolingual_v1",
                text=user_input
            )

            # Save audio
            audio_path = "output.mp3"
            with open(audio_path, "wb") as f:
                for chunk in audio_stream:
                    f.write(chunk)

            st.success("✅ Audio generated!")
            st.audio(audio_path, format="audio/mp3")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")






