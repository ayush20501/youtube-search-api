from fastapi import FastAPI
from youtubesearchpython import VideosSearch

app = FastAPI()

@app.get("/youtube-search")
def youtube_search(query: str, max_results: int = 5):
    try:
        videos_search = VideosSearch(query, limit=max_results * 2)
        results = []

        for video in videos_search.result()['result']:
            duration = video.get('duration', '')
            total_seconds = 0

            if duration: 
                time_parts = list(map(int, duration.split(':')))
                if len(time_parts) == 3: 
                    total_seconds = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
                elif len(time_parts) == 2:
                    total_seconds = time_parts[0] * 60 + time_parts[1]
            if total_seconds > 60:
                results.append({
                    "videoname": video['title'],
                    "videourl": video['link'],
                    "videoimage": video['thumbnails'][0]['url']
                })
                if len(results) >= max_results:
                    break

        return {"query": query, "videourls": results}

    except Exception as e:
        return {"error": str(e)}
