long puzzle2(char *s,char *d)
{
    for(char *curr_s = s;curr_s++)
    {
        char *curr_d = d;
        char c_d;

        do
        {
            c_d = *curr_d++;
            if(c_d == '\0')
            {
                return curr_s - s;
            }
        } while(*curr_s !=c_d);
    }


}