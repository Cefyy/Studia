from itertools import permutations

sl1 = input("Pierwsze słowo: ").upper()
op = input("Operator (+ - * /): ")
sl2 = input("Drugie słowo: ").upper()
sl3 = input("Wynik: ").upper()

litery = sorted(set(sl1 + sl2 + sl3))
if len(litery) > 10:
    print("Za dużo liter!")
    exit()

for cyfry in permutations('0123456789', len(litery)):
    t = dict(zip(litery, cyfry))
    if t[sl1[0]] == '0' or t[sl2[0]] == '0' or t[sl3[0]] == '0':
        continue
    a = int(''.join(t[c] for c in sl1))
    b = int(''.join(t[c] for c in sl2))
    c = int(''.join(t[c] for c in sl3))
    if op == '+' and a + b == c or \
       op == '-' and a - b == c or \
       op == '*' and a * b == c or \
       op == '/' and b != 0 and a / b == c:
        print(a, op, b, "=", c)
        break
else:
    print("Brak rozwiązania")