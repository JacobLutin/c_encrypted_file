#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	int sum;
	int i;

	if (argc == 2)
	{
		for (i = 0; i < strlen(argv[1]); i++)
		{
			sum += argv[1][i];
		}

		if (sum == 997)
		{
			printf("Access Granted!\n");
		}
		else
		{
			printf("WRONG\n");
		}
	}
	else
	{
		printf("Usage: <key>\n");
	}
	return 0;
}
