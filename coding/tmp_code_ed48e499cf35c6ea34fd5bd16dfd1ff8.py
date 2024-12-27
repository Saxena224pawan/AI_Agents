import requests
from bs4 import BeautifulSoup

# Search for papers related to Video Generation
search_terms = ["Video Generation", "SoRA", "Dreammachine", "NeRF"]
results = []

for term in search_terms:
    response = requests.get(f"https://arxiv.org/search/?query={term}&searchtype=all&source=header")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for entry in soup.find_all('li', {'class': 'arxiv-result'}):
        title = entry.find('p', {'class': 'title'}).text.strip()
        authors = entry.find('p', {'class': 'authors'}).text.strip()
        abstract = entry.find('p', {'class': 'abstract'}).text.strip()
        results.append({'title': title, 'authors': authors, 'abstract': abstract})

# Limit to 10 papers
results = results[:10]
for paper in results:
    print(f"Title: {paper['title']}")
    print(f"Authors: {paper['authors']}")
    print(f"Abstract: {paper['abstract']}\n")