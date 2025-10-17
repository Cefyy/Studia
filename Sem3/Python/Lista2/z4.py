import random
import requests



    
def scrape_txt(url):
    response = requests.get(url)
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
    tekst = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."
    uprosc_zdanie(scrape_txt(url),10,50)
    uprosc_zdanie(tekst,10,5)
