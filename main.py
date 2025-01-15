from fastapi import FastAPI
from pytube import Search
app = FastAPI()
@app.get("/youtube-search")
def youtube_search(query: str, max_results: int = 5):
    try:
        search = Search(query)
        results = []
        for video in search.results[:max_results]:
            results.append(f"https://www.youtube.com/watch?v={video.video_id}")
        return {"query": query, "results": results}
    except Exception as e:
        return {"error": str(e)}
