
//rdi - x  rsi - y
long decode(long x,long y)
{
    long temp = x + y;
    x = x^(temp);
    y = y^(temp);
    temp = x&y >> 63;


}