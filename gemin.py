Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... from elevenlabs import generate, play, set_api_key
... 
... # Set your ElevenLabs API key
... set_api_key("sk_e373223b3e4669fec91cbb030ec16e77099168e063d62081")
... 
... st.set_page_config(page_title="Text to Voice", layout="centered")
... st.title("🗣️ Text to Voice (ElevenLabs)")
... 
... # Text input box
... text_input = st.text_area("Enter text to speak:", height=150)
... 
... # Voice selection (optional)
... voice = st.selectbox("Choose a voice:", ["Rachel", "Bella", "Antoni", "Elli"])
... 
... # Submit button
... if st.button("Speak"):
...     if text_input.strip() == "":
...         st.warning("Please enter some text.")
...     else:
...         with st.spinner("Generating voice..."):
...             audio = generate(
...                 text=text_input,
...                 voice=voice,
...                 model="eleven_monolingual_v1"
...             )
...             st.success("✅ Voice ready!")
...             play(audio)
