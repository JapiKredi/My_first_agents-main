# filename: summarize_papers.py
from gensim.summarization import summarize

def text_to_summary(text, ratio=0.5):
    return summarize(text, ratio=ratio)

filenames = [f"paper{i+1}.txt" for i in range(5)]
texts = [open(fn, 'r').read() for fn in filenames]
summaries = [text_to_summary(text) for text in texts]

# Save summaries to text files
for i, summary in enumerate(summaries):
    with open(f"summary{i+1}.txt", 'w') as f:
        f.write(summary)