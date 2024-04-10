import os
import time
import requests
import argparse

def search_lyrics(title, api_base_url):
    url = f"{api_base_url}?title={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def save_lyrics(music_file, lyrics, output_dir):
    base_name = os.path.splitext(os.path.basename(music_file))[0]
    lyrics_file = os.path.join(output_dir, f"{base_name}.lrc")
    with open(lyrics_file, "w", encoding="utf-8") as file:
        file.write(lyrics)

def watch_folder(folder_path, api_base_url, output_dir):
    while True:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith((".mp3", ".wav", ".flac")):
                    music_file = os.path.join(root, file)
                    base_name = os.path.splitext(file)[0]
                    lyrics_file = os.path.join(output_dir, f"{base_name}.lrc")
                    if not os.path.exists(lyrics_file):
                        title = base_name
                        lyrics = search_lyrics(title, api_base_url)
                        if lyrics:
                            save_lyrics(music_file, lyrics, output_dir)
                            print(f"Lyrics saved for {file}")
                        else:
                            print(f"Lyrics not found for {file}")
        time.sleep(10)  # Wait for 10 seconds before scanning the folder again

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lyrics Watcher")
    parser.add_argument("folder_path", help="Path to the folder to watch for music files")
    parser.add_argument("api_base_url", help="Base URL of the lyrics API")
    parser.add_argument("output_dir", help="Directory to save the lyrics files")
    args = parser.parse_args()

    folder_path = args.folder_path
    api_base_url = args.api_base_url
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    watch_folder(folder_path, api_base_url, output_dir)
