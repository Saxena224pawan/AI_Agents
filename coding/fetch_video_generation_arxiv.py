# filename: fetch_video_generation_arxiv.py
import requests

def fetch_papers():
    url = "http://export.arxiv.org/api/query"
    query = "Video Generation"
    params = {
        "search_query": f"title:{query}",
        "start": 0,
        "max_results": 10,
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print("Error fetching papers:", response.status_code, response.text)
        return ""

def main():
    papers_feed = fetch_papers()
    print(papers_feed)

main()