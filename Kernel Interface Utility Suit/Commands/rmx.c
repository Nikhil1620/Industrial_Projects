#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>
#include<sys/utsname.h>

// 	./rmx   Filename
// 	argv[0]	argv[1]	
// 	argc = 2
//To delete (remove) a file from the filesystem.

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		printf("Error : Insufficient arguments\n");
		printf("Use as : ./rmx path\n");
		
		return -1;
	}
		
	if(access(argv[1], F_OK) == 0)
	{
		if(unlink(argv[1]) == -1)
		{
			printf("Error : Unable to delete\n");
			return -1;
		}
		else
		{
			printf("Success : File gets deleted\n");
		}	
	}
	else
	{
		printf("Error : Unable to delete as file is not persent\n");
		return -1;
	}
	return 0;
}