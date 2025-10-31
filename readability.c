#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    int letras = 0;
    int palavras = 1; // começa com 1
    int sentencas = 0;

    string text = get_string("Text: ");

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letras++;
        }
        else if (text[i] == ' ')
        {
            palavras++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentencas++;
        }
    }

    // Calcular L e S
    float L = ((float) letras / palavras) * 100;
    float S = ((float) sentencas / palavras) * 100;

    // Fórmula de Coleman-Liau
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Arredondar o índice
    int grau = round(index);

    // Mostrar o resultado
    if (grau < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grau >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grau);
    }
}
