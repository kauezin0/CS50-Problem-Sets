#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h> // Necessário para a função atoi()

// Protótipo da função de validação (para verificar se é só dígito)
bool only_digits(string s);

int main(int argc, string argv[])
{
    // 1. VALIDAÇÃO DOS ARGUMENTOS (argc)
    if (argc != 2 || !only_digits(argv[1]))
    {
        // Se o número de argumentos não for 2 OU se a chave não for um número
        printf("Usage: ./caesar key\n");
        return 1; // Retorna 1 para indicar erro
    }

    // 2. CONVERSÃO DA CHAVE E MÓDULO 26
    // Converte a chave (string) para um inteiro (int)
    int k = atoi(argv[1]);

    // Reduz a chave para o intervalo [0, 25] (k % 26)
    int key = k % 26;

    // 3. OBTENÇÃO DO TEXTO ORIGINAL (PLAINTEXT)
    string plaintext = get_string("Plaintext: ");

    // 4. INÍCIO DA CIFRAGEM (CIPHERTEXT)
    printf("Ciphertext: ");

    // Itera sobre cada caractere do texto original
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Verifica se é uma letra minúscula
        if (islower(c))
        {
            // Pega o índice da letra (0=a, 25=z)
            int index = c - 'a';
            // Aplica a cifra, garante o loop (módulo 26) e volta para o caractere minúsculo
            char ciphertext_char = (index + key) % 26 + 'a';
            printf("%c", ciphertext_char);
        }
        // Verifica se é uma letra maiúscula
        else if (isupper(c))
        {
            // Pega o índice da letra (0=A, 25=Z)
            int index = c - 'A';
            // Aplica a cifra, garante o loop (módulo 26) e volta para o caractere maiúsculo
            char ciphertext_char = (index + key) % 26 + 'A';
            printf("%c", ciphertext_char);
        }
        // Caractere não-alfabético (pontuação, espaços, números)
        else
        {
            // Imprime o caractere sem cifrar
            printf("%c", c);
        }
    }

    printf("\n"); // Nova linha após a saída
    return 0; // Retorna 0 para indicar sucesso
}

// IMPLEMENTAÇÃO DA FUNÇÃO AUXILIAR
bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // Se encontrar qualquer caractere que NÃO seja dígito, retorna falso
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}
