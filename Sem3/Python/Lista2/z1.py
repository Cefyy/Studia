def wybory(wyniki_wyborow,ilosc_mandatow):
    calkowite_glosy=sum(glosy for _,glosy in wyniki_wyborow)
    partie_powyzej = [(partie,glosy) for (partie,glosy) in wyniki_wyborow if glosy/calkowite_glosy >=0.05]  
    ilorazy = []
    for partia,glosy in partie_powyzej:
        for i in range(1,ilosc_mandatow+1):
            iloraz=glosy/i
            ilorazy.append((iloraz,partia))
    ilorazy.sort(reverse=True)
    
    mandaty={}
    for(partia,_) in partie_powyzej:
        mandaty[partia] =0
    for i in range(ilosc_mandatow):
        _,partia = ilorazy[i]
        mandaty[partia]+=1
        print(f"Mandat#{i+1}: {partia}")
    return mandaty


if __name__ == '__main__':
    wyniki = {("A",765), ("B",348),("C",356),("D",23)}
    mandaty = wybory(wyniki,8)
    print("\nWynik:")
    for partia,ilosc_mandatow in mandaty.items():
        print(f"{partia}: {ilosc_mandatow} mandatów" )