#include <stdio.h>


static size_t my_strlen(const char *s)
{
    size_t length = 0;
    
    while (s[length] != '\0')
     {
        length++;
    }
    
    return length;
}

const char *my_index(const char *s, char v) {
    for (size_t i = 0; i < my_strlen(s); i++)
        if (s[i] == v)
            return &s[i];
    return 0; }