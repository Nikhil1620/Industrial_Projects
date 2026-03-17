#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>

// 	./touchx  FileName
// 	argv[0]	 argv[1]	
// 	argc = 2

/*
	Accept file name from command line
	Check whether file is existing or not
	If it is existing return
	If it it is not existing
	Create that file
*/

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		printf("Error : Insufficient arguments\n");
		printf("Use as : ./touchx FileName\n");
		
		return -1;
	}

	if(access(argv[1], F_OK) == 0)
	{
		return 0;	
	}
	else
	{
		creat(argv[1],0777);
	}
	
	return 0;
}