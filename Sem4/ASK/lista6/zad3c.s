

.callOmit : pushq $.ReturnAdress
                pushq(% rdi, % rsi, 8)
                    ret
                        .ReturnAdress:
    // reszta kodu teoretycznie

    // znowu recznie wrzucamy returnadress do ramki imitując calla pozniej wrzucamy tam gdzie ma skoczyc
    // i jak ret sie wywoła w tamtej funkcji to wezmie nasz return adress i wroci tutaj