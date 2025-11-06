import requests
import re
from collections import defaultdict,Counter
from bs4 import BeautifulSoup

urls = ["https://www.geeksforgeeks.org/python/response-text-python-requests/",
        "https://www.geeksforgeeks.org/python/python-counter-objects-elements/",
        "https://docs.python.org/3/",
        "https://ii.uni.wroc.pl//"]

def scrape_text(url):
    try:
        html = requests.get(url)
        html.raise_for_status()
        soup = BeautifulSoup(html.text,features='html.parser')
        return soup.get_text(separator=" ")
    except Exception as e:
        print(f"Error {e} while scraping {url}")
        return ""
        
def build_index(urls):
    index = defaultdict(lambda: defaultdict(int))
    for url in urls:
        text = scrape_text(url)
        words = re.findall(r"[A-Za-zÀ-ÿ]+(?:['-][A-Za-zÀ-ÿ]+)*", text.lower())
        counter = Counter(words)
        for word,count in counter.items():
            index[word][url]+=count
    return index

def most_common_word(index):
    count_all = {word : sum(counts.values()) for word,counts in index.items()}
    word = max(count_all,key = count_all.get)
    return word,count_all.get(word)

def find_word(word,index):
    if word not in index:
        return ""
    else:
        return list(index[word].keys())
#======================================================================================#
index = build_index(urls)

word,count = most_common_word(index)
print(f"The most common word in our list of adresses is {word} with {count} occurences")

found_urls = find_word(word,index)
print(f"The word {word} is found in these urls: ")
for url in found_urls:
    print(url)

