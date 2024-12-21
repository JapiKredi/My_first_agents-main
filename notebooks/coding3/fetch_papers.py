# filename: fetch_papers.py
import requests
import xml.etree.ElementTree as ET
import json
from xmljson import badgerfish as bf

# Fetch papers using arXiv API
def fetch_papers(query, num_papers):
    url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': query,
        'max_results': num_papers,
        'sortBy': 'relevance',
        'sortOrder': 'descending'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        response_xml = response.text
        papers_json = xml_to_json(response_xml)
        papers = parse_papers_json(papers_json)
        return papers
    else:
        print(f"An error occurred while fetching the papers. Status Code: {response.status_code}")
        return []

# Convert XML response to JSON
def xml_to_json(xml_string):
    xml_parsed = ET.fromstring(xml_string)
    json_data = bf.data(xml_parsed)
    return json_data

# Parse papers from JSON response
def parse_papers_json(papers_json):
    papers = []
    entries = papers_json.get('feed', {}).get('entry', [])
    if isinstance(entries, dict):  # Single result
        entries = [entries]
    for entry in entries:
        title = entry.get('title', {}).get('$', '')
        authors = [author.get('name', {}).get('$', '') for author in entry.get('author', [])]
        abstract = entry.get('summary', {}).get('$', '')
        papers.append({
            'title': title,
            'authors': ', '.join(authors),
            'abstract': abstract
        })
    return papers

# Save papers to a Markdown file
def save_to_markdown(papers, filename):
    with open(filename, 'w') as file:
        for paper in papers:
            file.write(f"# {paper['title']}\n\n")
            file.write(f"- Authors: {paper['authors']}\n")
            file.write(f"- Abstract: {paper['abstract']}\n\n")

# Fetch and save the papers
query = 'using large language models to augment human productivity'
num_papers = 5
papers = fetch_papers(query, num_papers)
if papers:
    save_to_markdown(papers, 'research-report-llms-productivity.md')
    print("Papers fetched and summarization completed. Please check the 'research-report-llms-productivity.md' file.")
else:
    print("Failed to fetch papers. Please check your internet connection and try again.")