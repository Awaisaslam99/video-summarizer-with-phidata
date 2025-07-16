from phi.agent import Agent
from model.gemini_model import get_gemini_model, get_agent_tools
import streamlit as st

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=get_gemini_model(),
        tools=get_agent_tools(),
        markdown=True
    )
