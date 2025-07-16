import tempfile
from google.generativeai import upload_file, get_file
from pathlib import Path
import time

def save_temp_video(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp:
        temp.write(file.read())
        return temp.name

def process_video(video_path):
    uploaded_video = upload_file(video_path)
    while uploaded_video.state.name == "PROCESSING":
        time.sleep(1)
        uploaded_video = get_file(uploaded_video.name)
    return uploaded_video

def cleanup_temp_file(path):
    Path(path).unlink(missing_ok=True)
