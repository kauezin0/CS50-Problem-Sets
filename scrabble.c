#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Declaração de Variáveis

    int score[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                     1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int sum(int pts[], string words);

    // Entrada dos jogadores

    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");
    int pts_play1[strlen(player1)];
    int pts_play2[strlen(player2)];

    // loop score jogadores 1 e 2

    for (int i = 0; i < strlen(player1); i++)
    {
        player1[i] = toupper(player1[i]);

        if (isalpha(player1[i])) // só conta letras
        {
            pts_play1[i] = score[player1[i] - 'A'];
        }
        else
        {
            pts_play1[i] = 0; // qualquer outro caractere vale 0
        }
    }

    for (int i = 0; i < strlen(player2); i++)
    {
        player2[i] = toupper(player2[i]);
        if (isalpha(player2[i]))
        {
            pts_play2[i] = score[player2[i] - 'A'];
        }
        else
        {
            pts_play2[i] = 0;
        }
    }

    // chamada da função soma

    int soma1 = sum(pts_play1, player1);
    int soma2 = sum(pts_play2, player2);

    // Who won?

    if (soma1 > soma2)
    {
        printf("Player 1 wins!\n");
    }
    else if (soma2 > soma1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}

// função de soma

int sum(int pts[], string words)
{
    int soma = 0;

    for (int i = 0; i < strlen(words); i++)
    {
        soma += pts[i];
    }
    return soma;
}