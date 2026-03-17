#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>

// 	./cpx 	Source.txt 	Dest.txt
// 	argv[0]	 argv[1]	argv[2]

// 	argc = 3
//To copy the contents of one file (source) into another file (destination).

/*
	Open Source file for reading
	Create Destination file 
	Read the data from source
	Write it into destination
	close both files
*/

#define MAX_BUFFER_SIZE 1024

int main(int argc, char *argv[])
{
	if(argc != 3)
	{
		printf("Error : Insufficient arguments\n");
		printf("Use as : ./cpx SourceFileName DestinationFileName\n");
		
		return -1;
	}

	int fdSrc = 0, fdDest = 0, iRet = 0;
	char Buffer[MAX_BUFFER_SIZE] = {'\0'};
	
	memset(Buffer,'\0',sizeof(Buffer));
	
	fdSrc = open(argv[1],O_RDONLY);
	if(fdSrc < 0)
	{
		printf("Error : Unable to open source file : %s\n",argv[1]);
		return -1;
	}
	
	fdDest = creat(argv[2],0777);
	if(fdDest < 0)
	{
		printf("Error : Unable to create destination file : %s\n",argv[2]);
		close(fdSrc);
		return -1;
	}
	
	while((iRet = read(fdSrc,Buffer,sizeof(Buffer))) != 0)
	{
		write(fdDest,Buffer,iRet);
		memset(Buffer,'\0',sizeof(Buffer));
	}
	
	printf("Success : Copy activity done\n");
	
	close(fdSrc);
	close(fdDest);
	
	return 0;
}