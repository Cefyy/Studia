

pushq 0x4006f8(,%rsi,8)
ret

// imitujemy wywołanie calla który niejawnie wrzuca na wierzch stacka return adress, po prostu robiac to recznie a ret
// zdejmuje ta wartosc i wywołuje kod w nim