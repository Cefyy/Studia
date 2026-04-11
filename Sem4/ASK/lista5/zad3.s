.global ourcmp
# jesli x < y to rax = (-1) + (-1) + 1 = -1 działa
# jesli x=y to rdi = 0 rax = 0 i CF = 0 wiec rax = 0 + 0 + 0 = 0 działa
# jesli x > y to rdi = 1 rax = 0 + 0 + 1 = 1 działa
ourcmp:
    subq %rsi,%rdi #rdi = x - y jesli x<y to CF = 1 w.p.p CF = 0
    sbbq %rax,%rax #jesli -1 to CF było równe 1
    negq %rdi #jesli rdi = 0 to CF = 0 w.p.p CF = 1
    adcq %rax, %rax 

    ret
    