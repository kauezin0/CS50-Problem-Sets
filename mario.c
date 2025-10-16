#include <cs50.h>
#include <stdio.h>

int main(void)
{
    void pyramid(int height);

    int answer;

    do
    {

        answer = get_int("what is the heigth of the pyramid? ");
    }
    while (answer <= 0 || answer > 8);

    pyramid(answer);
}

void pyramid(int height)
{
    for (int i = 1; i <= height; i++)
    {

        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
