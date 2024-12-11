# Video Downloader and Uploader

This program is a Python-based solution for downloading videos from Instagram and TikTok, monitoring a directory for new video files, and uploading those files to a server. It also includes features for asynchronous video uploading and progress tracking.

## Features
- Download videos from Instagram and TikTok.
- Monitor a specified directory for new `.mp4` files.
- Automatically upload detected video files to a server.
- Asynchronous upload functionality with progress tracking.

## Requirements

### Python Version
- Python 3.7 or higher

### Libraries
Install the following libraries using `pip`:
```bash
pip install instaloader watchdog tqdm aiohttp requests TikTokApi
```

### TikTok API Setup
For TikTok video downloads, additional setup may be required:
```bash
pip install playwright
playwright install
```
Refer to the [TikTokApi documentation](https://github.com/davidteather/TikTok-Api) for details.

### API Tokens
- Obtain a valid `Flic-Token` from your server or API provider.
- Replace the placeholder `"your_flic_token_here"` in the code with your actual token.

### Directory Setup
- Create a directory for monitoring new video files. Example:
  - `C:\Users\arjun\OneDrive\Desktop\python projects\video downloader`

## Usage

### 1. Clone the Repository
Clone this project or copy the code into a local directory.

### 2. Prepare the Environment
Install the required libraries as mentioned above.

### 3. Set Up the Directory
Create the directory where the program will monitor for new `.mp4` files.

### 4. Run the Program
Save the script as `video_uploader.py` and run it:
```bash
python video_uploader.py
```

### 5. Test the Program
- Add a `.mp4` video file to the monitored directory.
- The program will automatically detect and upload the video.

## API Details

### Fetch Upload URL
The program uses the following endpoint to fetch a pre-signed upload URL:
```
GET https://api.socialverseapp.com/posts/generate-upload-url
```

### Upload Video
Uploads the `.mp4` video file to the pre-signed URL returned by the above endpoint.

### Create Post
Creates a new post after the video is successfully uploaded:
```
POST https://api.socialverseapp.com/posts
```
Payload example:
```json
{
  "title": "My Video",
  "hash": "video_hash",
  "is_available_in_public_feed": false,
  "category_id": 123
}
```

## File Structure
```plaintext
video_uploader.py      # Main program file
requirements.txt       # List of required libraries (optional)
README.md              # Documentation file
```

## Error Handling
- Ensure the `Flic-Token` is valid and has proper permissions.
- Verify that the API endpoints are reachable and return correct responses.
- Handle network interruptions and file permission errors gracefully.

## Contributing
Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

## Acknowledgments
- [Instaloader](https://instaloader.github.io/)
- [TikTokApi](https://github.com/davidteather/TikTok-Api)
- [Watchdog](https://github.com/gorakhargosh/watchdog)
