import streamlit as st
from elevenlabs import generate, play, set_api_key

set_api_key("sk_d8d152a907bffbd400af0bab528ca9bb6f7a5e9b73a81f0a")  # Replace with your real API key

st.set_page_config(page_title="AI Voice Doubt Solver")
st.title("🎙️ AI Voice Doubt Solver")
st.markdown("Ask your doubt in the chat and hear the answer in your teacher's voice!")

user_input = st.text_input("Type your question here 👇")

if user_input:
    with st.spinner("Generating voice response..."):
        try:
            audio = generate(
                text=user_input,
                voice="Sarah",  # You can change this voice ID
                model="eleven_multilingual_v2"
            )

            with open("output.mp3", "wb") as f:
                f.write(audio)

            st.audio("output.mp3", format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")



