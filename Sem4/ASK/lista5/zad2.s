.global oblicz
.global oblicz_z_sbb


# x jest w rdi y w rsi wynik w rax

oblicz:
    movq %rdi,%rax
    addq %rsi,%rax

    jc overflow

    ret

overflow:
    movq $-1,%rax
    ret


# wersja z sbb dodajemy x i y w rax, pozniej odejmujemy rax od samego siebie z CF, jesli było przepełnienie to 0-1 = -1 czyli ULONG MAX

oblicz_z_sbb:
    movq %rdi,%rax
    addq %rsi,%rax

    sbbq %rdx,%rdx

    orq %rdx,%rax

    ret
