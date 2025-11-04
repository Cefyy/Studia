import requests
from bs4 import BeautifulSoup
from collections import defaultdict,Counter
import re

urls = ["https://www.geeksforgeeks.org/python/response-text-python-requests/",
        "https://www.geeksforgeeks.org/python/python-counter-objects-elements/",
        "https://docs.python.org/3/"]
def scrape_text(url):
    try:
        html = requests.get(url,timeout=5)
        html.raise_for_status()
        soup = BeautifulSoup(html.text,features="html.parser")
        return soup.get_text(separator= " ")
    except Exception as e:
        print(f"Error while scraping {url}: {e}")
        return ""

def build_index(urls):
    index = defaultdict(lambda: defaultdict(int))
    for url in urls:
        text = scrape_text(url)
        words = re.findall(r"\w+",text.lower())
        counter = Counter(words)
        for word,count in counter.items():
            index[word][url] += count
            
    return index


def most_frequent_word(index):
    counters = { word: sum(counts.values()) for word,counts in index.items()}
    word = max(counters,key=counters.get)
    return word,counters.get(word)

def find_where(index,word):
    if word not in index:
        return []
    return list(index[word].keys())
index = build_index(urls)
word,count = most_frequent_word(index)
print(f"Najpopularniejsze słowo: '{word}' ({count} wystąpień)")
print(f"Występuje na stronach:")
for url in find_where(index, word):
    print(" -", url)
word1="tutorial"
print(f"Slowo {word1} znajduje sie na: ")
for url in find_where(index, word1):
    print(" -",url)
word1="geeksforgeeks"
print(f"Slowo {word1} znajduje sie na: ")
for url in find_where(index, word1):
    print(" -",url)
    