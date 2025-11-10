import requests
import re
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
import threading
urls = [
    "https://www.geeksforgeeks.org/python/response-text-python-requests/",
    "https://www.geeksforgeeks.org/python/python-counter-objects-elements/",
    "https://docs.python.org/3/",
    "https://ii.uni.wroc.pl//",
]

lock = threading.Lock()
def scrape_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, features='html.parser')
        return soup.get_text(separator=" ")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error while scraping {url}: {e}")
        return ""
def process_url(url,index):
    text = scrape_text(url)
    if not text:
        return
    words = re.findall(r"[A-Za-zÀ-ÿ]+(?:['-][A-Za-zÀ-ÿ]+)*", text.lower())
    counter = Counter(words)
    
    with lock:
        for word, count in counter.items():
            index[word][url] += count
    return index

def build_index(urls):
    index = defaultdict(lambda: defaultdict(int))
    threads = []
    for url in urls:
        t= threading.Thread(target=process_url,args=(url,index))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    return index
    

def most_common_word(index):
    if not index:
        return None, 0
    count_all = {word: sum(counts.values()) for word, counts in index.items()}
    word = max(count_all, key=count_all.get)
    return word, count_all.get(word)

def find_word(word, index):
    return list(index.get(word, {}).keys())

# ====================================================================================== #

index = build_index(urls)

word, count = most_common_word(index)
if word:
    print(f"The most common word in our list of addresses is '{word}' with {count} occurrences.")
    found_urls = find_word(word, index)
    print(f"The word '{word}' is found in these URLs:")
    for url in found_urls:
        print(f" - {url}")
else:
    print("No words found. Possibly all pages failed to load.")

word1 = "requests"
word2 = "list"
print(find_word(word1,index))
print(find_word(word2,index))