# filename: fetch_video_generation_papers.py
import requests

def fetch_papers():
    url = "https://api.semanticscholar.org/v1/paper/search"
    query = "Video Generation"
    params = {
        "query": query,
        "offset": 0,
        "limit": 10,
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        papers = response.json().get("data", [])
        return [(paper["title"], paper["paperId"]) for paper in papers]
    else:
        print("Error fetching papers:", response.status_code, response.text)
        return []

def main():
    papers = fetch_papers()
    if papers:
        for title, paper_id in papers:
            print(f"Title: {title}, Paper ID: {paper_id}")
    else:
        print("No papers found.")

main()