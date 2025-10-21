# This script retrieves the top 100 trending videos from YouTube's Data API (v3) 
# and saves the raw JSON data into a file.
# It handles API pagination to fetch more than the 50-item limit.

import os
import json
from googleapiclient.discovery import build
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_trending_videos(region_code='TR', max_count=100):
    """
    Fetches up to 100 trending videos from YouTube by handling pagination.
    """
    if not API_KEY:
        print("Error: YOUTUBE_API_KEY not found in environment variables.")
        return []

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # YouTube API max per page is 50. We need 2 requests for 100.
    videos = []
    next_page_token = None
    
    print(f"Fetching {max_count} trending videos for region {region_code}...")

    # Fetch loop
    for i in range(2):
        request = youtube.videos().list(
            part='snippet,statistics',
            chart='mostPopular',
            regionCode=region_code,
            maxResults=50,  # Max allowed per request
            pageToken=next_page_token
        )
        
        try:
            response = request.execute()
            
            # Add videos to the main list
            videos.extend(response.get('items', []))
            
            # Get the token for the next page
            next_page_token = response.get('nextPageToken')
            
            print(f"  > Successfully fetched {len(response.get('items', []))} videos (Total: {len(videos)})")

            # Break if no more pages are available or we hit the max count
            if not next_page_token or len(videos) >= max_count:
                break
                
        except Exception as e:
            print(f"An error occurred during API call: {e}")
            break

    # Truncate to max_count if we overshot slightly
    return videos[:max_count]

def save_data_to_file(video_data):
    """
    Saves the fetched video data to a JSON file.
    """
    final_data = {
        "fetch_region": "TR",
        "fetch_timestamp": "null", # We use null as LLM will fill in current date
        "video_count": len(video_data),
        "trending_videos_list": video_data
    }
    
    file_path = 'trending_videos_data.json'
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(final_data, f, ensure_ascii=False, indent=2)
        print(f"\nSuccessfully saved {len(video_data)} videos to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == '__main__':
    video_data = get_trending_videos()
    if video_data:
        save_data_to_file(video_data)
# --- EOF ---
