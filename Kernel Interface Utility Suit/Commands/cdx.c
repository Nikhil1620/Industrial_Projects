#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>

// 	./cdx  	 DirectoryPath
// 	argv[0]	 argv[1]	
// 	argc = 2
//To change the current working directory of the program to 
// a user-specified path and display the new directory.

/*
	Accept new directory path
	Call chdir with that path
	Call getcwd to check the changed path
*/

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		printf("Error : Insufficient arguments\n");
		printf("Use as : ./cdx DirectoyPath\n");
		
		return -1;
	}

	if(chdir(argv[1]) == -1)
	{
		printf("Error : Unable to change current directory\n");
		
		return -1;
	}
	
	char Buffer[256] = {'\0'};
	
	getcwd(Buffer,sizeof(Buffer)-1);
	
	printf("Current directory changed to %s\n",Buffer);
	
	// open
	
	return 0;
}