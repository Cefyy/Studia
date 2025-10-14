import random
import sys
import requests

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    
def scrape_txt(url):
    response = requests.get(url)
    response.raise_for_status()
    response.encoding= 'utf-8'
    return response.text
def uprosc_zdanie(tekst: str, dl_slowa: int, liczba_slow: int) -> None:
    
    tokens = tekst.split()
    tokens = [s for s in tokens if len(s) < dl_slowa and s.isalpha()]


    while len(tokens) > liczba_slow:
        idx = random.randrange(len(tokens))
        tokens.pop(idx)

    wynik = " ".join(tokens)
    print(wynik)


if __name__ == '__main__':
    url = "https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt"
    uprosc_zdanie(scrape_txt(url),5,750)
