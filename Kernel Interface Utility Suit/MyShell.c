#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/wait.h>

#define MAX 100

int main()
{
    char input[MAX];
    char *args[MAX];

    while(1)
    {
        // Display prompt
        printf("MyShell > ");

        // Read input
        if(fgets(input, sizeof(input), stdin) == NULL)
        {
            continue;
        }

        // Remove newline
        input[strcspn(input, "\n")] = 0;

        // Skip empty input
        if(strlen(input) == 0)
        {
            continue;
        }

        // Exit command
        if(strcmp(input, "exit") == 0)
        {
            printf("Exiting MyShell...\n");
            break;
        }

        // Tokenize input into arguments
        int i = 0;
        args[i] = strtok(input, " ");

        while(args[i] != NULL && i < MAX-1)
        {
            i++;
            args[i] = strtok(NULL, " ");
        }

        // 🔥 Built-in command: cd (IMPORTANT)
        if(strcmp(args[0], "cdx") == 0)
        {
            if(args[1] == NULL)
            {
                printf("cdx: missing argument\n");
            }
            else
            {
                if(chdir(args[1]) != 0)
                {
                    printf("cdx: unable to change directory\n");
                }
            }
            continue;
        }

        // Create child process
        int pid = fork();

        if(pid < 0)
        {
            printf("Error: Fork failed\n");
        }
        else if(pid == 0)
        {
            // Child process executes command
            execvp(args[0], args);

            // If exec fails
            printf("Error: Command not found\n");
            exit(0);
        }
        else
        {
            // Parent waits
            wait(NULL);
        }
    }

    return 0;
}