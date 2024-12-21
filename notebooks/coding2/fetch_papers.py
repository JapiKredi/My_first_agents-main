# filename: fetch_papers.py
import requests

# Fetch papers using Semantic Scholar API
def fetch_papers(query, num_papers):
    headers = {
        'Accept': 'application/json'
    }
    params = {
        'query': query,
        'limit': num_papers
    }
    response = requests.get('https://api.semanticscholar.org/v1/paper/search', headers=headers, params=params)
    papers = response.json()['results']
    return papers

# Save papers to a Markdown file
def save_to_markdown(papers, filename):
    with open(filename, 'w') as file:
        for paper in papers:
            title = paper['title'].replace('\n', ' ').replace('#', '')
            abstract = paper['abstract'].replace('\n', ' ').replace('#', '')
            authors = ', '.join(a['name'] for a in paper['authors'])
            citation_count = paper['citationCount']

            file.write(f"# {title}\n\n")
            file.write(f"- Authors: {authors}\n")
            file.write(f"- Citation Count: {citation_count}\n")
            file.write(f"- Abstract: {abstract}\n\n")

# Fetch and save the papers  
query = 'using large language models to augment human productivity'
num_papers = 5
papers = fetch_papers(query, num_papers)
save_to_markdown(papers, 'research-report-llms-productivity.md')
print("Papers fetched and summarization completed. Please check the 'research-report-llms-productivity.md' file.")