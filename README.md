Lyrics Downloader
Lyrics Downloader is a Python script that automatically searches and downloads missing lyrics for music files in a specified folder. It uses a lyrics API to fetch the lyrics and saves them as .lrc files with the same naming as the corresponding music files. The script runs inside a Docker container, making it easy to deploy and run on any system.

Features
Watches a specified folder for music files (supports .mp3, .wav, and .flac formats)
Searches for missing lyrics using a configurable lyrics API
Downloads and saves the lyrics as .lrc files with the same naming as the music files
Runs continuously in the background, periodically checking for new music files
Configurable API base URL and output directory
Runs inside a Docker container for easy deployment and portability
Prerequisites
Docker installed on your system
Usage
Clone the repository:
```shell
git clone https://github.com/yaurora/lycdownloader.git
```
Navigate to the project directory:
```shell
cd lycdownloader
```
Build the Docker image:
```shell
docker build -t lycdownloader .
```
Run the Docker container:
```shell
docker run -v /path/to/music/folder:/music -v /path/to/lyrics/output:/lyrics lycdownloader
```
Replace /path/to/music/folder with the actual path to the folder containing your music files, and /path/to/lyrics/output with the path where you want to store the downloaded lyrics files.

The script will start watching the specified folder for music files and download the missing lyrics. The downloaded lyrics will be saved as .lrc files in the specified output directory.
Configuration
The script accepts the following command-line arguments:

folder_path: Path to the folder to watch for music files (default: /music)
api_base_url: Base URL of the lyrics API (default: https://lrc.xms.mx/lyrics)
output_dir: Directory to save the lyrics files (default: /lyrics)
You can modify the default values in the Dockerfile's CMD instruction or pass the arguments when running the Docker container.

Customization
To use a different lyrics API, update the api_base_url argument in the Dockerfile's CMD instruction or pass it as a command-line argument when running the Docker container.
Recommended: https://github.com/HisAtri/LrcApi

If you want to support additional music file formats, modify the watch_folder function in the lyrics_watcher.py script to include the desired file extensions.

License
This project is licensed under the MIT License.
