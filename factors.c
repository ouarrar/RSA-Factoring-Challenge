#include "factors.h"

/**
 * main - main function
 *
 * Return: void
 */
int main(int argc, char *argv[])
{
	FILE *file;
	size_t counter;
	ssize_t line;
	char *buffer = NULL;


	if (argc != 2)
	{
		fprintf(stderr, "Usage: factors <filename>\n");
		exit(EXIT_FAILURE);
	}

	file = fopen(argv[1], "r");
	if (file == NULL)
	{
		fprintf(stderr, "Error: can't open file %s\n", argv[1]);
		exit(EXIT_FAILURE);
	}

	while ((line = getline(&buffer, &counter, file)) != -1)
	{
		factorize(buffer);
	}

	return (0);
}
