
import requests
from datetime import datetime, timedelta
from flask import current_app


def get_recent_videos(query, page_token=''):
   
    
    
    published_after = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')


    # trying all key 
    api_keys = current_app.config['YOUTUBE_API_KEY']
    if not api_keys:
        current_app.logger.error("No API keys configured")
        return {'videos': [], 'error': "No API keys configured"}
        
    errors = []
    
    # iterating over all key 
    for key_index, api_key in enumerate(api_keys):
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'order': 'date',
            'publishedAfter': published_after,
            'key': api_key,
            'maxResults': current_app.config['RESULTS_PER_PAGE'],
            'pageToken': page_token
        }
        
        try:
            current_app.logger.info(f"Trying YouTube API key {key_index+1}/{len(api_keys)}")
            response = requests.get(current_app.config['YOUTUBE_API_URL'], params=params)
            
            # is exhausted what to do
            if response.status_code == 403 and 'quotaExceeded' in response.text:
                current_app.logger.warning(f"API key {key_index+1} quota exceeded, trying next key")
                errors.append(f"Key {key_index+1}: Quota exceeded")
                continue
                
            
            response.raise_for_status()
            
            
            data = response.json()
            items = data.get('items', [])
            
            #video format
            videos = [
                {
                    'videoId': item['id']['videoId'],
                    'title': item['snippet']['title'],
                    'video_url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    'published_at': item['snippet']['publishedAt'],
                    'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                    'channel': item['snippet']['channelTitle'],
                    'description': item['snippet'].get('description', '')
                }
                for item in items
            ]
            
            current_app.logger.info(f"Successfully fetched {len(videos)} videos using API key {key_index+1}")
            
            return {
                'videos': videos,
                'next_token': data.get('nextPageToken'),
                'prev_token': data.get('prevPageToken')
            }
            
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"YouTube API error with key {key_index+1}: {str(e)}")
            errors.append(f"Key {key_index+1}: {str(e)}")
    
    # all key failed
    current_app.logger.error(f"All YouTube API keys failed: {errors}")
    return {
        'videos': [],
        'next_token': None,
        'prev_token': None,
        'error': f"All API keys failed: {'; '.join(errors)}"
    }