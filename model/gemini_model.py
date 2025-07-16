from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

def get_gemini_model():
    return Gemini(id="gemini-2.0-flash-exp")

def get_agent_tools():
    return [DuckDuckGo()]
