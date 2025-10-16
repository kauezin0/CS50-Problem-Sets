#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int troco(int change);
    int answer;

    do
    {
        answer = get_int("change owed: ");
    }
    while (answer <= 0);

    troco(answer);
}

int troco(int change)
{

    int m = 0;

    while (change >= 25)
    {
        change -= 25;
        m++;
    }

    while (change >= 10)
    {
        change -= 10;
        m++;
    }

    while (change >= 5)
    {
        change -= 5;
        m++;
    }

    while (change >= 1)
    {
        change -= 1;
        m++;
    }
    printf("%i\n", m);
    return m;
}
