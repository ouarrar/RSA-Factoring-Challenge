#include "factors.h"

/**
 * factorize - Factorizes an integer and prints its factors.
 * @buffer: A character array containing the integer to factorize.
 *
 * This function takes a character array and attempts to factorize the
 * integer represented by the characters in the buffer. It prints the
 * factorization if a factor is found.
 *
 * Return: 0
 */
int factorize(char *buffer)
{

	u_int32_t num;
	u_int32_t i;

	num = atoi(buffer);


	for (i = 2; i < num; i++)
	{
		if (num % i == 0)
		{
			printf("%d=%d*%d\n", num, num / i, i);
			break;
		}
	}
	return (0);
}
