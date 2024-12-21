# filename: save_papers.py

# Define the paper information
papers = [
    {
        'title': 'Paper title 1',
        'authors': ['Author 1', 'Author 2'],
        'citation_count': 10,
        'abstract': 'Summary of the first paper goes here.'
    },
    {
        'title': 'Paper title 2',
        'authors': ['Author 3', 'Author 4'],
        'citation_count': 15,
        'abstract': 'Summary of the second paper goes here.'
    },
    {
        'title': 'Paper title 3',
        'authors': ['Author 5', 'Author 6'],
        'citation_count': 8,
        'abstract': 'Summary of the third paper goes here.'
    },
    {
        'title': 'Paper title 4',
        'authors': ['Author 7', 'Author 8'],
        'citation_count': 12,
        'abstract': 'Summary of the fourth paper goes here.'
    },
    {
        'title': 'Paper title 5',
        'authors': ['Author 9', 'Author 10'],
        'citation_count': 20,
        'abstract': 'Summary of the fifth paper goes here.'
    }
]

# Save papers to Markdown file
filename = 'research-report-llms-productivity.md'
with open(filename, 'w') as file:
    file.write('# Research Report: Use of Large Language Models to Augment Human Productivity\n\n')

    for index, paper in enumerate(papers, start=1):
        file.write(f'## Paper {index}: {paper["title"]}\n')
        file.write(f'- Authors: {", ".join(paper["authors"])}\n')
        file.write(f'- Citation Count: {paper["citation_count"]}\n')
        file.write(f'- Abstract: {paper["abstract"]}\n\n')
    
print(f"Papers saved to '{filename}'.")