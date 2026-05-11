Przy leaf wywołuje się n+1 razy, poniewaz kompilator nie wie czy funkcja modyfikuje argumenty czy nie
Przy pure tylko raz przed ponieważ kompilator wie że funkcja nie modyfikuje s wiec odpala raz przed pętlą
Zmieniamy na static, przez co ograniczamy widoczność tylko do tego pliku, i funkcja nadal wywołuje się n+1 razy,
ale inlining spowodował że wywołanie naszej funkcji zostało zastąpione bibliotecznym strlen
Kompilatorowi nie udało sie wywnioskować że funkcja jest czysta

