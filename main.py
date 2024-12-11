import os
import time
import requests
import asyncio
import aiohttp
from tqdm import tqdm
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def delete_local_video(file_path):
    """Delete a video file from the local system."""
    if os.path.exists(file_path):
        os.remove(file_path)

def download_instagram_video(post_url: str, save_path: str):
    """Download a video from Instagram."""
    import instaloader
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, post_url)
    loader.download_post(post, target=save_path)

async def upload_video_async(file_path: str, upload_url: str):
    """Upload a video file asynchronously."""
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'rb') as f:
            async with session.put(upload_url, data=f) as response:
                if response.status == 200:
                    print(f"Uploaded {file_path} successfully.")
                    return True
                else:
                    print(f"Failed to upload {file_path}. Status: {response.status}")
                    return False

def get_upload_url():
    """Get a pre-signed upload URL from the server."""
    headers = {
        "Flic-Token": "flic_1034abf4225fbf903ee5f2352c22d7b78eda65c5191f6c3aa881bb9674d80fc3",
        "Content-Type": "application/json"
    }
    response = requests.get("https://api.socialverseapp.com/posts/generate-upload-url", headers=headers)
    if response.status_code == 200:
        return response.json().get("https://drive.google.com/drive/folders/1av9mFfpbo6MoewzmQ3bs85Sqr7BwDo4Q?usp=drive_link")
    else:
        print("Failed to get upload URL:", response.status_code, response.text)
        return None

class VideoHandler(FileSystemEventHandler):
    """Handle new video files in the directory."""
    async def on_created(self, event):
        if event.src_path.endswith('.mp4'):
            upload_url = get_upload_url()
            if upload_url:
                await upload_video_async(event.src_path, upload_url)

def monitor_directory(directory):
    """Monitor a directory for new video files."""
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    video_directory = r"C:\Users\arjun\OneDrive\Desktop\python projects\video downloader"
    if os.path.exists(video_directory):
        monitor_directory(video_directory)
    else:
        print(f"Directory {video_directory} does not exist. Please create it and try again.")





