#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    uint8_t buffer[512];
    char buffer2[12];
    int count = 0;
    FILE *img = NULL;

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {

            if (img != NULL) // Se já tem um arquivo aberto (não é o primeiro)
            {
                fclose(img);
            }

            sprintf(buffer2, "%03i.jpg", count);
            img = fopen(buffer2, "w");
            fwrite(buffer, 1, 512, img);
            count++;
        }
        else
        {
            if (img != NULL)
            {
                fwrite(buffer, 1, 512, img);
            }
        }
    }
    if (img != NULL)
    {
        fclose(img);
    }
        fclose(card);
}
