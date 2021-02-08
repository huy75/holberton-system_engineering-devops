#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - Create 5 zombie processes
 * Return: 0
 */
int main(void)
{
	unsigned int idx;
	size_t pid;

	for (idx = 0; idx < 5; idx++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();

	return (0);
}
