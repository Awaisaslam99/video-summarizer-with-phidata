import streamlit as st
import os
from dotenv import load_dotenv

from controller.agent_controller import initialize_agent
from utils.video_utils import save_temp_video, process_video, cleanup_temp_file
from view.interface import (
    render_header, render_video_uploader, get_user_query,
    render_analysis_result, render_custom_styles
)

# Load environment
load_dotenv()
import google.generativeai as genai

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

render_header()
render_custom_styles()

agent = initialize_agent()
video_file = render_video_uploader()

if video_file:
    video_path = save_temp_video(video_file)
    st.video(video_path)

    user_query = get_user_query()

    if st.button("🔍 Analyze Video"):
        if not user_query:
            st.warning("Please enter a question.")
        else:
            with st.spinner("Analyzing video..."):
                try:
                    processed = process_video(video_path)
                    prompt = (
                        f"Analyze the uploaded video for content and context.\n"
                        f"Respond to the following query using video insights and web research:\n"
                        f"{user_query}\n\nProvide a detailed and user-friendly response."
                    )
                    result = agent.run(prompt, videos=[processed])
                    render_analysis_result(result)
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    cleanup_temp_file(video_path)
else:
    st.info("Upload a video to begin.")
