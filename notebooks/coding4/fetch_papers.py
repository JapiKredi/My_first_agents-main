# filename: fetch_papers.py
import requests
import re

# Fetch arXiv papers using API
def fetch_papers(query, num_papers):
    base_url = "http://export.arxiv.org/api/query?"
    query = query.replace(' ', '+')
    url = f"{base_url}search_query=all:{query}&max_results={num_papers}&sortBy=submittedDate&sortOrder=descending"
    response = requests.get(url)
    return response.text

# Extract relevant information from arXiv papers
def extract_information(papers):
    regex = r"<title>(.*?)<\/title>.*<author>(.*?)<\/author>.*<summary>(.*?)<\/summary>"
    matches = re.findall(regex, papers, re.DOTALL)
    return matches

# Save papers to a Markdown file
def save_to_markdown(papers, filename):
    with open(filename, 'w') as file:
        for title, authors, summary in papers:
            title = title.replace('\n', ' ').replace('#', '')
            authors = authors.replace('\n', ' ').replace('#', '')
            summary = summary.replace('\n', ' ').replace('#', '')

            file.write(f"# {title}\n\n")
            file.write(f"- Authors: {authors}\n")
            file.write(f"- Summary: {summary}\n\n")

# Fetch and save the papers
query = 'using large language models to augment human productivity'
num_papers = 5

try:
    papers = fetch_papers(query, num_papers)
    extracted_papers = extract_information(papers)
    save_to_markdown(extracted_papers, 'research-report-llms-productivity.md')
    print("Papers fetched and summarization completed. Please check the 'research-report-llms-productivity.md' file.")
except Exception as e:
    print("An error occurred while fetching or summarizing papers:")
    print(str(e))