# 🎥 Video Summarizer AI Agent with PhiData, Gemini & DuckDuckGo

A smart, multimodal AI-powered video summarization tool that uses **PhiData Agents**, **Gemini 2.0 Flash**, and **DuckDuckGo** for research augmentation. Built with a clean **MVC structure** and a beautiful UI powered by **Streamlit**, this tool allows users to upload videos and ask insightful questions — generating rich, context-aware responses.

---

## 🚀 Features

- 🎬 Upload and analyze videos in `.mp4`, `.avi`, or `.mov` formats
- 🧠 Leverages Gemini 2.0 Flash (via Google Generative AI)
- 🌐 Uses DuckDuckGo for real-time web context augmentation
- 💬 Accepts natural language questions about the video content
- ⚙️ Structured using MVC (Model-View-Controller) for maintainability
- 🎨 Custom-styled Streamlit UI for clean interaction

---

## 🧠 Tech Stack

| Layer         | Tool / Framework             |
|---------------|------------------------------|
| LLM           | Gemini 2.0 Flash (Google)     |
| AI Agent      | [Phi](https://github.com/phidatahq/phi) Agent Framework |
| Web Search    | DuckDuckGo Tool               |
| Frontend UI   | Streamlit                     |
| Structure     | MVC (Model-View-Controller)   |
| Environment   | Python + dotenv               |

---

## 📁 Project Structure

video-summarizer-with-phidata/
├── app.py # Main controller and app entry point
├── controller/
│ └── agent_controller.py # Initializes the Phi agent
├── model/
│ └── gemini_model.py # Loads Gemini model and tools
├── view/
│ └── interface.py # Streamlit UI components
├── utils/
│ └── video_utils.py # Video upload and processing functions
├── requirements.txt # Project dependencies
└── README.md # Project documentation



---

## 🔑 Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Awaisaslam99/video-summarizer-with-phidata.git
cd video-summarizer-with-phidata


Install Dependencies
pip install -r requirements.txt


▶️ Run the App
bash
Copy
Edit
streamlit run app.py


📄 License
MIT License — Free to use and modify with attribution.

🙋 Author
Built by Awais Aslam
Connect on GitHub for more AI-powered projects.

---
