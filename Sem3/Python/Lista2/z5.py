
import requests


def scrape_txt(url):
    response = requests.get(url)
    response.encoding= 'utf-8'
    return response.text

def kompresja(tekst : str):
    tekst = tekst.split()
    wynik=[]
    for word in tekst:
        length = len(word)
        licznik=1
        for i in range(1,length):

            if(word[i]==word[i-1]):
                licznik+=1
            else:
                wynik.append((word[i-1],licznik))
                licznik=1
        wynik.append((word[length-1],licznik))
        wynik.append((' ',1))
    return wynik
                    
            
def dekompresja(tekst_skompresowany):
    decoded=""
    for krotka in tekst_skompresowany:
        currletter,currcnt = krotka
        for i in range(0,currcnt):
            decoded=decoded+currletter
    return decoded
            
if __name__ == '__main__':
    #url = "https://wolnelektury.pl/media/book/txt/treny-tren-viii.txt"
    #url2= "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    #compressedTren=kompresja(scrape_txt(url))
   # decompressedTren=dekompresja(compressedTren)
    compressed = kompresja("aaab! bbbbccd, dddd!")
    decompressed = dekompresja(compressed)
    #compressedEng=kompresja(scrape_txt(url2))
    #decompressedEng=dekompresja(compressedEng)
    #print(compressedTren)
    #print(decompressedTren)
    print(compressed)
    print(decompressed)
    #print(compressedEng)
    #print(decompressedEng)

