# bed_summary.py
# Scrape and summarize Adm. William McRaven's "Make Your Bed" speech.
# Note to self: This speech is plain text from a more sophisticated webpage than MLK's speech. Is the scraping process different?

import requests
import bs4
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize # Gensim removed summarize from versions > gensim==3.8.3. Use `pip install gensim==3.8.3` to maintain this functionality.

url = 'https://jamesclear.com/great-speeches/make-your-bed-by-admiral-william-h-mcraven'
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
p_elems = [element.text for element in soup.find_all('p')]

speech = ' '.join(p_elems)

# Summarize the speech
print("\nSummary of Make Your Bed speech:")
summary = summarize(speech, word_count=225) # Summarize also allows a `ratio` option. E.g., `ratio=0.01` would produce a summary whose length is 1% of the original document.
sentences = sent_tokenize(summary)
sents = set(sentences) # Sets are unordered, so the summary arrangement may change with multiple runs.
print(' '.join(sents)) # Don't combine print and summarize. It may duplicate sentences.