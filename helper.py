#YOUTUBE RELATED HELPERS.....

from api_service import get_video_details, get_youtube_service, search_videos
from utils import calculate_rating, calculate_title_relevance_score


def find_top_rated_videos(api_key, topics):
    youtube = get_youtube_service(api_key)
    all_results = {}

    for topic in topics:
        videos = search_videos(youtube, topic)
        if isinstance(videos, str):
            return videos  # Return the error message if an error occurred
        
        results = []
        for video in videos:
            video_id = video.get('video_id')
            if not video_id:
                continue

            video_details = get_video_details(youtube, video_id)
            if isinstance(video_details, str):
                return video_details  # Return the error message if an error occurred
            
            title_relevance_score = calculate_title_relevance_score(video.get('title', ''), topic)
            
            if video_details.get('comments', 0) >= 20:
                rating = calculate_rating(video_details, title_relevance_score)
                
                results.append({
                    'title': video.get('title', 'No Title'),
                    'channel_name': video.get('channel_title', 'No Channel Name'),
                    'date_uploaded': video.get('published_at', 'Unknown Date'),
                    'rating': rating,
                    'url': video.get('url', '#'),
                    'video_id': video_id
                })
        
        results.sort(key=lambda x: x['rating'], reverse=True)
        all_results[topic] = results[:1]  # Get top 1 video for each topic
    
    return all_results


