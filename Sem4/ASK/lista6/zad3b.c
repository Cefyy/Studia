void exec(void (**f)(void),long index)
{
    f[index]();
}