import streamlit as st

def render_header():
    st.set_page_config(page_title="Video Summarizer", page_icon="🎥", layout="wide")
    st.title("Phidata Video AI Summarizer Agent 🎥🎤🖬")
    st.header("Powered by Gemini 2.0 Flash Exp")

def render_video_uploader():
    return st.file_uploader("Upload a video file", type=['mp4', 'mov', 'avi'], help="Upload a video for AI analysis")

def get_user_query():
    return st.text_area(
        "What insights are you seeking from the video?",
        placeholder="Ask anything about the video content...",
        help="Provide specific questions or insights."
    )

def render_analysis_result(response):
    st.subheader("Analysis Result")
    st.markdown(response.content)

def render_custom_styles():
    st.markdown("""
        <style>
        .stTextArea textarea { height: 100px; }
        </style>
    """, unsafe_allow_html=True)
