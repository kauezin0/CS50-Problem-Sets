// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

node *cere = NULL;
unsigned int contador = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    int index = hash(word);
    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{

    int b;

    unsigned long hash_v = 5381;

    while ((b = *word++))
    {
        b = tolower(b);
        hash_v = ((hash_v << 5) + hash_v) + b;
    }

    return hash_v % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *source = fopen(dictionary, "r");

    if (source == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];

    while (fscanf(source, "%s", buffer) != EOF)
    {
        node *new_node = malloc(sizeof(node));

        if (new_node == NULL)
        {
            return false;
        }

        strcpy(new_node->word, buffer);
        unsigned int ls = hash(buffer);
        new_node->next = table[ls];
        table[ls] = new_node;

        contador++;
    }

    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return contador;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor->next;
            free(cursor);
            cursor = tmp;
        }
    }
    return true;
}
