import streamlit as st
from elevenlabs import generate, play, set_api_key

# 🔑 Set your ElevenLabs API Key
set_api_key("sk_229b14396cd72ee09a6d24e45ac351439c25cc9961305b0b")  # Replace with your actual API key

st.set_page_config(page_title="AI Voice Doubt Solver")
st.title("🎙️ AI Voice Doubt Solver")
st.markdown("Ask your doubt in the chat and hear the answer in your teacher's voice!")

# 📝 User input
user_input = st.text_input("Type your question here 👇")

if user_input:
    with st.spinner("Generating voice response..."):
        try:
            # 🎤 Generate voice using ElevenLabs
            audio = generate(
                text=user_input,
                voice="Sarah",  # You can change to your preferred voice
                model="eleven_multilingual_v2"
            )

            # 💾 Save to file
            with open("output.mp3", "wb") as f:
                f.write(audio)

            # 🔊 Play in Streamlit
            st.audio("output.mp3", format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")















